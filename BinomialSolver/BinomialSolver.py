#!/usr/bin/env python

import sys, re

def isValidInput(string):
    # fix regex ... it allows (+)^number
    result = re.match(r'\([-]?([1-9]+[0-9]*)*([a-z](\^[1-9]+[0-9]*)?)*[+-]([1-9]+[0-9]*)*([a-z](\^[1-9]+[0-9]*)?)*\)\^[1-9]+[0-9]*', string)
    return result != None and result.group(0) == string

def badInput():
    print 'Error: incorrect input. Expected the following format:'
    print '   --> (<a>[+,-]<b>)^<n>, where a,b,n can contain any'
    print '   --> valid combination of variables and positive ints,'
    print '   --> but n must only contain positive ints.'

def splitAB(ab):
    a     = '-' if ab[0] == '-' else ''
    b     = '-' if '+' not in ab else ''
    ab    = ab[1:] if ab[0] == '-' else ab
    split = ab.split('+') if '+' in ab else ab.split('-')
    
    a += split[0]
    b += split[1]

    return (a, b)

def getVariables(string):
    a = ''
    b = ''
    
    ab, n = string.split(')')
    n     = n.replace('^', '')
    ab    = ab.replace('(', '')
    split = splitAB(ab)
    a, b  = ('', '') if len(split) != 2 else split

    return (a, b, n)

def choose(n, k):
    factorials = [n, n-k, k]
    results    = []

    for factorial in factorials:
        total = 1
        
        for i in xrange(1, factorial + 1):
            total *= i

        results += [total]

    return results[0] / (results[1] * results[2])

def solveBinomial(a, b, n):
    finals = []
    for k in xrange(n + 1):
        finals += ['(%i)(%s)^%i(%s)^%i' % (choose(n, k), a, n - k, b, k)]

    print ' + '.join(finals) 

def main(argc, argv):
    if argc == 1 and isValidInput(argv[0]):
        a, b, n = getVariables(argv[0])
        print 'a = ' + a 
        print 'b = ' + b 
        print 'n = ' + n


        if a == '' or b == '':
            badInput()

        solveBinomial(a, b, int(n))
    else:
        badInput()

if __name__ == '__main__':
   main(len(sys.argv) - 1, sys.argv[1:])