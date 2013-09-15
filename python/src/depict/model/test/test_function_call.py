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
from depict.model.function_call import FunctionCall
from depict.model.util.repo import Repo
from depict.model.util.tree import RootNode
from mock import patch
import unittest

class TestFunctionCall(unittest.TestCase):
    def setUp(self):
        self.thread = RootNode()

    def test_creation(self):
        FunctionCall('fake_function_call_id', 'fake_function_id', self.thread)

    def test_a_function_call_knows_which_function_was_called(self):
        with patch('depict.model.function_call.global_function_repo', Repo()) as function_repo_mock:
            fake_function_id = 'fake_function_id'
            expected_function = Function(fake_function_id, 'function_name')
            function_repo_mock.add(expected_function)
            function_call = FunctionCall('dummy_id', fake_function_id, self.thread)

            actual_function = function_call.function

            self.assertEqual(actual_function, expected_function)
