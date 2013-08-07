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

from mock import Mock, patch, PropertyMock, ANY, mock_open, call
from depict.processing.function_call_notifier import FunctionCallNotifier
from depict.model.class_repo import GlobalClassRepo
from depict.model.function_repo import GlobalFunctionRepo
from depict.processing.class_definition_collector import ClassDefinitionCollector
from depict.processing.function_definition_collector import FunctionDefinitionCollector

class TestFunctionCallNotifier():
    def test_init_creates_thread_scoped_tracer(self):
        with patch('depict.processing.function_call_notifier.ThreadScopedTracer') as tracerClass_mock:
            tracer_mock = Mock()
            tracerClass_mock.return_value = tracer_mock
            function_call_notifier = FunctionCallNotifier(Mock())
            tracerClass_mock.assert_called_once_with(function_call_notifier)

    def test_start_creates_thread_scoped_tracer(self):
        with patch('depict.processing.function_call_notifier.ThreadScopedTracer') as tracerClass_mock:
            tracer_mock = Mock()
            tracerClass_mock.return_value = tracer_mock
            function_call_notifier = FunctionCallNotifier(Mock())
            function_call_notifier.start()
            tracer_mock.start.assert_called_once_with()

    def test_stop_stops_thread_scoped_tracer(self):
        with patch('depict.processing.function_call_notifier.ThreadScopedTracer') as tracerClass_mock:
            tracer_mock = Mock()
            tracerClass_mock.return_value = tracer_mock
            function_call_notifier = FunctionCallNotifier(Mock())
            function_call_notifier.start()
            function_call_notifier.stop()
            tracer_mock.stop.assert_called_once_with()

    def test_processes_static_data_for_each_call(self):
        with patch('depict.processing.function_call_notifier.GlobalDefinitionCollectionOrchestrator') as global_definition_collector_orchestrator_mock:
            observer_mock = Mock()
            function_call_notifier = FunctionCallNotifier(observer_mock)
            frame_digest_mock = Mock()
            type(frame_digest_mock).function_name = PropertyMock(return_value='fake_function_name')
            type(frame_digest_mock).file_name = PropertyMock(return_value='fake_file_name')
            type(frame_digest_mock).line_number = PropertyMock(return_value=1)
            function_call_notifier.on_call(frame_digest_mock)
            calls = [call(ClassDefinitionCollector), call(FunctionDefinitionCollector)]
            global_definition_collector_orchestrator_mock.include.assert_has_calls(calls)
            global_definition_collector_orchestrator_mock.process.assert_called_once_with('fake_file_name')
