#!/usr/bin/env python

import sys, re

def isValidInput(string):
    # fix regex ... it allows (+)^number
    result = re.match(r'\([-]?([1-9]+[0-9]*)*([a-z](\^[1-9]+[0-9]*)?)*[+-]([1-9]+[0-9]*)*([a-z](\^[1-9]+[0-9]*)?)*\)\^[1-9]+[0-9]*', string)
    return result != None and result.group(0) == string

def getVariables(string):
    a = ''
    b = ''
    
    ab, n = string.split(')')
    n     = n.replace('^', '')
    ab    = ab.replace('(', '')
    split = ab.split('+')
    a, b  = ('', '') if len(split) != 2 else split

    return (a, b, n)

def badInput():
    print 'Error: incorrect input. Expected the following format:'
    print '   --> (<a>[+,-]<b>)^<n>, where a,b,n can contain any'
    print '   --> valid combination of variables and positive ints,'
    print '   --> but n must only contain positive ints.'

def main(argc, argv):
    if argc == 1 and isValidInput(argv[0]):
        a, b, n = getVariables(argv[0])
        print a + ', ' + b + ', ' + n
        #TODO: generate the end formula and then replace with a, b, n and solve...?

        if a == '' or b == '':
            badInput()
    else:
        badInput()


if __name__ == '__main__':
   main(len(sys.argv) - 1, sys.argv[1:])