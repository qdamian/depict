# Copyright 2013 Damian Quiroga
#
# This file is part of Depict.
#
# Depict is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Depict is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Depict.  If not, see <http://www.gnu.org/licenses/>.

from depict.output.toy.function_call_list import FunctionCallList
from depict.output.toy.definition_list import DefinitionList
from formic.formic import FileSet

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
    file_set = FileSet(directory='.', include=[__file__])
    definition_list = DefinitionList(file_set, 'hello_world.definition_list.out')
    definition_list.run()

    function_call_list = FunctionCallList('hello_world.function_call_list.out', '.')
    function_call_list.start()
    main()
    function_call_list.stop()
