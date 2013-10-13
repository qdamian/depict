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

from depict.core.model.entity.method import Method
from depict.test.object_factory import real, unique


class TestClass():
    def test_creation(self):
        # Arrange nothing
        # Act
        real('Class_')
        # Asserting that no exceptions are raised

    def test_add_one_method(self):
        class_ = real('Class_')
        method = Method('dummy_id', 'dummy_name', class_)
        class_.add_method(method)

    def test_eq_comparison(self):
        class_1 = real('Class_')
        class_2 = real('Class_')
        assert_equal(class_1, class_2)

    def test_not_eq_comparison(self):
        class_1 = unique(real('Class_'))
        class_2 = unique(real('Class_'))
        assert_not_equal(class_1, class_2)
