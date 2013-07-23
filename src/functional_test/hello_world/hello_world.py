#!/usr/bin/env python

from depict.representation.function_list import FunctionList

def say_hi():
    print 'hello world'

def main():
    p = Person()
    p.say_hi()
    p.say_bye()

class Person():
    def say_hi(self):
        print 'Hello, world'

    def say_bye(self):
        print 'Bye'

if __name__ == '__main__':
    function_list = FunctionList('out_file')
    function_list.start()
    main()
    function_list.stop()
