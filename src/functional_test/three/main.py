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

#!/usr/bin/env python

from depict.presentation.toy.function_call_list import FunctionCallList
from depict.presentation.toy.definition_list import DefinitionList

from one import One
import two
from op import Addition

def main():
    print 'In main function'
    n_one = One()
    n_two = two.Two()
    print 'And the winner is: %s' % Addition(n_one, n_two)

if __name__ == '__main__':
    function_call_list = FunctionCallList('three.function_call_list.out')
    definition_list = DefinitionList(__file__, 'three.definition_list.out')
    function_call_list.start()
    main()
    function_call_list.stop()
    definition_list.run()
