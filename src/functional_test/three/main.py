#!/usr/bin/env python

from depict.presentation.toy.function_list import FunctionList

from one import One
import two
from op import Addition

def main():
    print 'In main function'
    n_one = One()
    n_two = two.Two()
    print 'And the winner is: %s' % Addition(n_one, n_two)

if __name__ == '__main__':
    function_list = FunctionList('three.out')
    function_list.start()
    main()
    function_list.stop()
