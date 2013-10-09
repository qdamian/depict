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

from depict.modeling.def_collection_orchestrator import AlreadyProcessed
from depict.modeling.function_call_notifier import FunctionCallNotifier
from depict.test.template import fake, real
from mock import Mock, patch, ANY
from nose.tools import assert_equal

class TestFunctionCallNotifier():
    def setUp(self):
        self.thread_scoped_tracer_patcher = patch('depict.modeling.function_call_notifier.ThreadScopedTracer', autospec=True)
        self.thread_scoped_tracer = fake('ThreadScopedTracer')
        self.thread_scoped_tracer_class = self.thread_scoped_tracer_patcher.start()
        self.thread_scoped_tracer_class.return_value = self.thread_scoped_tracer

        self.function_call_collector_patcher = patch('depict.modeling.function_call_notifier.FunctionCallCollector', autospec=True)
        self.function_call_collector = fake('FunctionCallCollector')
        self.function_call_collector_class = self.function_call_collector_patcher.start()
        self.function_call_collector_class.return_value = self.function_call_collector

        self.observer = Mock()
        self.def_collection_orchestrator = fake('DefCollectionOrchestrator')
        self.init_args = (self.observer,
                          fake('EntityIdGenerator'),
                          self.def_collection_orchestrator)

    def tearDown(self):
        self.thread_scoped_tracer_patcher.stop()
        self.function_call_collector_patcher.stop()

    def test_init_creates_thread_scoped_tracer(self):
        # Arrange nothing
        # Act
        function_call_notifier = FunctionCallNotifier(*self.init_args)

        # Assert
        self.thread_scoped_tracer_class.assert_called_once_with(function_call_notifier)
        self.function_call_collector_class.assert_called_once_with(ANY, ANY)

    def test_start_creates_thread_scoped_tracer(self):
        # Arrange nothing
        function_call_notifier = FunctionCallNotifier(*self.init_args)

        # Act
        function_call_notifier.start()

        # Assert
        self.thread_scoped_tracer.start.assert_called_once_with()

    def test_stop_stops_thread_scoped_tracer(self):
        # Arrange
        function_call_notifier = FunctionCallNotifier(*self.init_args)
        function_call_notifier.start()

        # Act
        function_call_notifier.stop()

        # Assert
        self.thread_scoped_tracer.stop.assert_called_once_with()

    def test_on_call_notifies_function_call_to_the_observer(self):
        # Arrange
        frame_digest = fake('FrameDigest', spec_set=False)
        expected_function_call = real('FunctionCall')
        self.function_call_collector.on_call.return_value = expected_function_call

        # Act
        function_call_notifier = FunctionCallNotifier(*self.init_args)
        function_call_notifier.on_call(frame_digest)

        # Assert
        self.observer.on_call.assert_called_once_with(ANY)
        actual_function_call = self.observer.on_call.call_args[0][0]
        assert_equal(actual_function_call.function, expected_function_call.function)

    def test_it_processes_static_data_for_each_call(self):
        # Arrange
        frame_digest = fake('FrameDigest')
        frame_digest.function_name = 'fake_function_name'
        frame_digest.file_name = 'fake_file_name'
        frame_digest.line_number = 1

        # Act
        function_call_notifier = FunctionCallNotifier(*self.init_args)
        function_call_notifier.on_call(frame_digest)

        # Assert
        self.def_collection_orchestrator.process.assert_called_once_with('fake_file_name')

    def test_it_ignores_already_processed_exception_for_static_data(self):
        # Arrange
        self.def_collection_orchestrator.process.side_effect = AlreadyProcessed

        # Act
        function_call_notifier = FunctionCallNotifier(*self.init_args)
        function_call_notifier.on_call(fake('FrameDigest'))

        # Asserting no exception is raised