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

from depict.model.function import Function
import unittest

class TestFunction(unittest.TestCase):
    def test_creation(self):
        Function('fake_function_id', 'fake_function_name')

    def test_equal_comparison(self):
        function1 = Function('fake_id1', 'dummy_name1')
        function2 = Function('fake_id1', 'dummy_name2')
        self.assertEqual(function1, function2)