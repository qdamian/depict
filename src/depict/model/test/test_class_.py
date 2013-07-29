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

from depict.model.class_ import Class_
from depict.model.method import Method
import unittest

class TestClass(unittest.TestCase):
    def test_creation(self):
        Class_('fake_class_id', 'fake_class_name')

    def test_add_one_method(self):
        class_ = Class_('dummy_class_id', 'dummy_class_name')
        method = Method('dummy_id', 'dummy_name', class_)
        class_.add_method(method)

    def test_eq_comparison(self):
        class_1 = Class_('fake_class_id1', 'dummy_class_name1')
        class_2 = Class_('fake_class_id1', 'dummy_class_name2')
        self.assertEqual(class_1, class_2)