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

from nose.tools import *

from depict.test.object_factory import real, unique


class TestMethod():
    def test_creation(self):
        real('Method')

    def test_eq_comparison(self):
        method1 = real('Method')
        method2 = real('Method')
        assert_equal(method1, method2)

    def test_not_eq_comparison(self):
        method1 = unique(real('Method'))
        method2 = unique(real('Method'))
        assert_not_equal(method1, method2)
