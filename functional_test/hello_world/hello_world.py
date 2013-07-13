#!/usr/bin/env python

from depict.plain_text import function_list

def say_hi():
    print 'hello world'

def main():
    say_hi()

if __name__ == '__main__':
    function_list.start('out_file')
    main()
    function_list.stop()

    expected_output = ['main\n', 'say_hi\n']
    with open('out_file', 'r') as f:
        actual_output = f.readlines()
        assert actual_output == expected_output
