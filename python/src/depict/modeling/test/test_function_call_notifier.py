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
from mock import Mock, patch
from nose.tools import assert_equal
from depict.test.template import fake
from depict.model.entity.thread import Thread

@patch('depict.modeling.function_call_notifier.ThreadScopedTracer')
class TestFunctionCallNotifier():
    def setUp(self):
        self.init_args = (fake('generic_observer'),
                          fake('EntityIdGenerator'),
                          fake('DefCollectionOrchestrator'))
        self.observer = Mock()
        self.def_collection_orchestrator = fake('DefCollectionOrchestrator')
        self.function_call_notifier = FunctionCallNotifier(self.observer,
                                                      fake('EntityIdGenerator'),
                                                      self.def_collection_orchestrator)

    def test_init_creates_thread_scoped_tracer(self, tracer_class):
        # Arrange nothing
        # Act
        function_call_notifier = FunctionCallNotifier(*self.init_args)

        # Assert
        tracer_class.assert_called_once_with(function_call_notifier)

    @patch('depict.modeling.function_call_notifier.threading', autospec=True)
    @patch('depict.modeling.function_call_notifier.EntityRepo', autospec=True)
    def test_init_creates_a_thread_entity_for_the_current_thread(self,
                                                                 entity_repo_class,
                                                                 threading,
                                                                 tracer_class):
        # Arrange
        thread = Mock()
        thread.name = 'FakeMainThread'
        threading.current_thread = Mock(return_value=thread)

        entity_repo = fake('EntityRepo')
        entity_repo_class.return_value = entity_repo

        # Act
        FunctionCallNotifier(*self.init_args)

        # Assert
        expected_thread = Thread(thread.name)
        entity_repo.add.assert_called_with(expected_thread)

    def test_start_creates_thread_scoped_tracer(self, tracer_class):
        # Arrange
        tracer = fake('ThreadScopedTracer')
        tracer_class.return_value = tracer

        # Act
        function_call_notifier = FunctionCallNotifier(*self.init_args)
        function_call_notifier.start()

        # Assert
        tracer.start.assert_called_once_with()

    def test_stop_stops_thread_scoped_tracer(self, tracer_class):
        # Arrange
        tracer = fake('ThreadScopedTracer')
        tracer_class.return_value = tracer

        # Act
        function_call_notifier = FunctionCallNotifier(*self.init_args)
        function_call_notifier.start()
        function_call_notifier.stop()

        # Assert
        tracer.stop.assert_called_once_with()

    def test_it_processes_static_data_for_each_call(self, tracer_class):
        # Arrange
        frame_digest = fake('FrameDigest')
        frame_digest.function_name = 'fake_function_name'
        frame_digest.file_name = 'fake_file_name'
        frame_digest.line_number = 1

        # Act
        self.function_call_notifier.on_call(frame_digest)

        # Assert
        self.def_collection_orchestrator.process.assert_called_once_with('fake_file_name')

    def test_it_ignores_already_processed_exception_for_static_data(self, tracer_class):
        # Arrange
        self.def_collection_orchestrator.process.side_effect = AlreadyProcessed

        # Act
        self.function_call_notifier.on_call(fake('FrameDigest'))

        # Asserting no exception is raised

    def test_it_relates_nested_function_calls(self, tracer_class):
        # Act
        self.function_call_notifier.on_call(fake('FrameDigest'))
        parent_function_call = self.observer.on_call.call_args[0][0]
        self.function_call_notifier.on_call(fake('FrameDigest'))
        child_function_call = self.observer.on_call.call_args[0][0]

        # Assert
        assert_equal(child_function_call.parent, parent_function_call)

    def test_it_considers_returns_when_relating_nested_function_calls(self, tracer_class):
        # Arrange nothing

        # Act
        self.function_call_notifier.on_call(fake('FrameDigest'))

        self.function_call_notifier.on_call(fake('FrameDigest'))
        child_function_call1 = self.observer.on_call.call_args[0][0]
        self.function_call_notifier.on_return(Mock())

        self.function_call_notifier.on_call(fake('FrameDigest'))
        child_function_call2 = self.observer.on_call.call_args[0][0]

        # Assert
        assert_equal(child_function_call1.parent, child_function_call2.parent)
