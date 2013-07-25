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

from depict.model.function_call import FunctionCall
from depict.model.function import Function
from depict.model.function_repo import GlobalFunctionRepo
import unittest

class TestFunctionCall(unittest.TestCase):
    def test_creation(self):
        FunctionCall('fake_function_id')
        
    def test_function_property(self):
        fake_function_id = 'fake_function_id'
        expected_function = Function('function_name', fake_function_id)
        GlobalFunctionRepo.add(expected_function)
        function_call = FunctionCall(fake_function_id)
        actual_function = function_call.function
        self.assertEqual(actual_function, expected_function)
        
    