#!/usr/bin/env python

from depict.representation.function_list import FunctionList

def say_hi():
    print 'hello world'

def main():
    say_hi()

if __name__ == '__main__':
    function_list = FunctionList('out_file')
    function_list.start()
    main()
    function_list.stop()

    expected_output = ['main\n', 'say_hi\n']
    with open('out_file', 'r') as f:
        actual_output = f.readlines()
        assert actual_output == expected_output
