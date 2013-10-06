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
from depict.model.entity.function_call import FunctionCall
from depict.model.util.entity_repo import EntityRepo
from depict.model.util.tree import TreeRootNode
from mock import patch, Mock
from nose.tools import assert_equal
from depict.model.model import Model
from depict.test.template import real

class TestFunctionCall():
    def setUp(self):
        self.thread = TreeRootNode()

    def test_creation(self):
        FunctionCall('fake_function_call_id', 'fake_function_id', self.thread, Mock())

    def test_a_function_call_knows_which_function_was_called(self):
        expected_function = real('Function')
        function_id = expected_function.id_
        model_mock = Model()
        model_mock.functions.add(expected_function)
        function_call = FunctionCall('dummy_id', function_id, self.thread, model_mock)

        actual_function = function_call.function

        assert_equal(actual_function, expected_function)
