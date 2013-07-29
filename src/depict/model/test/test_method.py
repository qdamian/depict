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

from depict.model.method import Method
import unittest

class TestMethod(unittest.TestCase):
    def test_creation(self):
        Method('fake_function_name',
                   'fake_function_id',
                   'fake_parent')
        
    def test_eq_comparison(self):
        method1 = Method('fake_id1', 'dummy_function_name1', 'dummy_parent1')
        method2 = Method('fake_id1', 'dummy_function_name2', 'dummy_parent2')
        self.assertEqual(method1, method2)
