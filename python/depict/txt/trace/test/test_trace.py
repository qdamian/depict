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

import sys

from mock import patch, Mock, ANY
from nose_parameterized import parameterized

from depict.test.object_factory import fake, real
from depict.txt.trace.trace import Trace


class TestTrace():
    def setUp(self):
        self.original_tracer = sys.gettrace()

        self.model_patcher = patch('depict.txt.trace.trace.ObservableModel')
        self.model_class = self.model_patcher.start()
        self.model = fake('ObservableModel')
        self.model_class.return_value = self.model
        
        self.function_call_notifier_patcher = patch('depict.txt.trace.trace.DynamicModelingDriver')
        self.dynamic_modeler_driver = fake('DynamicModelingDriver')
        function_call_notifier_class = self.function_call_notifier_patcher.start()
        function_call_notifier_class.return_value = self.dynamic_modeler_driver
        self.trace = Trace('.')

    def tearDown(self):
        self.model_patcher.stop()
        self.function_call_notifier_patcher.stop()
        self.original_tracer = sys.settrace(self.original_tracer)

    def test_it_provides_a_start_method_that_starts_tracing_calls(self):
        # Arranged in setUp
        # Act
        self.trace.start()

        # Assert
        self.dynamic_modeler_driver.start.assert_called_once_with()

    @parameterized.expand([('foo',), ('bar',)])
    def test_it_outputs_the_name_of_the_called_functions(self, function_name):
        # Arrange
        function_call = fake('FunctionCall')
        function_call.function.name = function_name
        self.trace.output = Mock()

        # Act
        self.trace.handle(function_call)

        # Assert
        self.trace.output.assert_called_once_with(module=ANY, msg=function_name, actor=ANY)

    @parameterized.expand([('Foo',), ('foo.bar',)])
    def test_it_outputs_the_name_of_actors(self, method_or_module_name):
        # Arrange
        function_call = fake('FunctionCall')
        function_call.function.parent.name = method_or_module_name
        self.trace.output = Mock()

        # Act
        self.trace.handle(function_call)

        # Assert
        self.trace.output.assert_called_once_with(module=ANY, msg=ANY, actor=method_or_module_name)

    def test_it_provides_a_stop_method_that_starts_tracing_calls(self):
        # Arranged in setUp
        # Act
        self.trace.stop()

        # Assert
        self.dynamic_modeler_driver.stop.assert_called_once_with()
