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

from depict.test.template import fake, real
from depict.txt.trace.trace_repr import TraceRepr
from mock import patch, Mock, ANY, call
from nose_parameterized import parameterized

class TestTraceRepr():
    def setUp(self):
        self.model_patcher = patch('depict.txt.trace.trace_repr.Model')
        self.model_class = self.model_patcher.start()
        self.model = real('Model')
        self.model_class.return_value = self.model
        
        self.function_call_notifier_patcher = patch('depict.txt.trace.trace_repr.FunctionCallNotifier')
        self.function_call_notifier = fake('FunctionCallNotifier')
        function_call_notifier_class = self.function_call_notifier_patcher.start()
        function_call_notifier_class.return_value = self.function_call_notifier
        self.trace_repr = TraceRepr('.')

    def tearDown(self):
        self.model_patcher.stop()
        self.function_call_notifier_patcher.stop()

    def test_it_provides_a_start_method_that_starts_tracing_calls(self):
        # Arranged in setUp
        # Act
        self.trace_repr.start()

        # Assert
        self.function_call_notifier.start.assert_called_once_with()

    @parameterized.expand([('foo',), ('bar',)])
    def test_it_outputs_the_name_of_the_called_functions(self, function_name):
        # Arrange
        function_call = fake('FunctionCall')
        function_call.function.name = function_name
        self.trace_repr.output = Mock()

        # Act
        self.trace_repr.on_call(function_call)

        # Assert
        self.trace_repr.output.assert_called_once_with(msg=function_name, actor=ANY)

    @parameterized.expand([('Foo',), ('foo.bar',)])
    def test_it_outputs_the_name_of_actors(self, method_or_module_name):
        # Arrange
        function_call = fake('FunctionCall')
        function_call.function.parent.name = method_or_module_name
        self.trace_repr.output = Mock()

        # Act
        self.trace_repr.on_call(function_call)

        # Assert
        self.trace_repr.output.assert_called_once_with(msg=ANY, actor=method_or_module_name)

    def test_it_provides_a_stop_method_that_starts_tracing_calls(self):
        # Arranged in setUp
        # Act
        self.trace_repr.stop()

        # Assert
        self.function_call_notifier.stop.assert_called_once_with()
