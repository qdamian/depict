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

from mock import Mock, patch, PropertyMock
from depict.modeling.function_call_notifier import FunctionCallNotifier
from depict.modeling.def_collection_orchestrator import AlreadyProcessed
from depict.model.entity.thread import Thread
from nose.tools import assert_equal

@patch('depict.modeling.function_call_notifier.ThreadScopedTracer')
class TestFunctionCallNotifier():
    def test_init_creates_thread_scoped_tracer(self, tracer_class_mock):
            tracer_mock = Mock()
            tracer_class_mock.return_value = tracer_mock

            function_call_notifier = FunctionCallNotifier(Mock(), Mock(), Mock())
            tracer_class_mock.assert_called_once_with(function_call_notifier)

    @patch('depict.modeling.function_call_notifier.threading')
    @patch('depict.modeling.function_call_notifier.global_thread_repo')
    def test_init_creates_a_thread_entity_for_the_current_thread(self, tracer_class_mock, thread_repo_mock, threading_mock):
        thread_mock = Mock()
        thread_mock.name = 'FakeMainThread'
        threading_mock.current_thread = Mock(return_value=thread_mock)
        FunctionCallNotifier(Mock(), Mock(), Mock())

    def test_start_creates_thread_scoped_tracer(self, tracer_class_mock):
        tracer_mock = Mock()
        tracer_class_mock.return_value = tracer_mock
        function_call_notifier = FunctionCallNotifier(Mock(), Mock(), Mock())
        function_call_notifier.start()
        tracer_mock.start.assert_called_once_with()

    def test_stop_stops_thread_scoped_tracer(self, tracer_class_mock):
        tracer_mock = Mock()
        tracer_class_mock.return_value = tracer_mock
        function_call_notifier = FunctionCallNotifier(Mock(), Mock(), Mock())
        function_call_notifier.start()
        function_call_notifier.stop()
        tracer_mock.stop.assert_called_once_with()

    def test_processes_static_data_for_each_call(self, tracer_class_mock):
        def_collection_orchestrator_mock = Mock()
        observer_mock = Mock()
        function_call_notifier = FunctionCallNotifier(Mock(), observer_mock, def_collection_orchestrator_mock)
        frame_digest_mock = Mock()
        type(frame_digest_mock).function_name = PropertyMock(return_value='fake_function_name')
        type(frame_digest_mock).file_name = PropertyMock(return_value='fake_file_name')
        type(frame_digest_mock).line_number = PropertyMock(return_value=1)
        function_call_notifier.on_call(frame_digest_mock)
        def_collection_orchestrator_mock.process.assert_called_once_with('fake_file_name')

    def test_ignores_already_processed_exception_for_static_data(self, tracer_class_mock):
        def_collection_orchestrator_mock = Mock()
        def_collection_orchestrator_mock.process.side_effect = AlreadyProcessed
        function_call_notifier = FunctionCallNotifier(Mock(), Mock(), def_collection_orchestrator_mock)
        frame_digest_mock = Mock()

        function_call_notifier.on_call(frame_digest_mock)
        # No exception raised

    def test_relates_nested_function_calls(self, tracer_class_mock):
        observer_mock = Mock()
        function_call_notifier = FunctionCallNotifier(observer_mock, Mock(), Mock())

        function_call_notifier.on_call(Mock())
        parent_function_call = observer_mock.on_call.call_args[0][0]
        function_call_notifier.on_call(Mock())
        child_function_call = observer_mock.on_call.call_args[0][0]

        assert_equal(child_function_call.parent, parent_function_call)

    def test_considers_returns_when_relating_nested_function_calls(self, tracer_class_mock):
        observer_mock = Mock()
        function_call_notifier = FunctionCallNotifier(observer_mock, Mock(), Mock())

        function_call_notifier.on_call(Mock())

        function_call_notifier.on_call(Mock())
        child_function_call1 = observer_mock.on_call.call_args[0][0]
        function_call_notifier.on_return(Mock())

        function_call_notifier.on_call(Mock())
        child_function_call2 = observer_mock.on_call.call_args[0][0]

        assert_equal(child_function_call1.parent, child_function_call2.parent)
