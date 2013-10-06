# Copyright 2013 Damian Quiroga
#
# This file is part of depict.
#
# depict is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# depict is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with depict.  If not, see <http://www.gnu.org/licenses/>.

from depict.model.entity.function import Function
from depict.test.template import fake, real, unique
from nose.tools import assert_equal, assert_not_equal

class TestFunction():
    def test_creation(self):
        fake('Function')

    def test_equal_comparison(self):
        function1 = real('Function')
        function2 = real('Function')
        assert_equal(function1, function2)

    def test_non_equal_comparison(self):
        function1 = unique(real('Function'))
        function2 = unique(real('Function'))
        assert_not_equal(function1, function2)