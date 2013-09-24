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
from depict.output.toy.def_list import DefList
from formic.formic import FileSet
import os

from one import One
import two
from op import Addition

def main():
    print 'In main function'
    n_one = One()
    n_two = two.Two()
    print 'And the winner is: %s' % Addition(n_one, n_two)

if __name__ == '__main__':
    file_set = FileSet(directory=os.path.abspath(os.path.dirname(__file__)), include='*.py')
    def_list = DefList(file_set, 'three.def_list.out')
    def_list.run()
    function_call_list = FunctionCallList('three.function_call_list.out', file_set.directory)
    function_call_list.start()
    main()
    function_call_list.stop()
