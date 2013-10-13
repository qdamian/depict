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

from depict.core.model.entity.thread import Thread
from depict.core.modeling.function_call_collector import FunctionCallCollector
from depict.test.object_factory import fake
from mock import Mock, patch
from nose.tools import *

@patch('depict.core.modeling.function_call_collector.threading', autospec=True)
class TestFunctionCallCollector:
    def setUp(self):
        self.entity_id_generator = fake('EntityIdGenerator')
        self.model = fake('Model')

    def test_init_creates_a_thread_entity_for_the_current_thread(self, threading):
        # Arrange
        thread = Mock()
        thread.name = 'FakeMainThread'
        threading.current_thread = Mock(return_value=thread)

        # Act
        FunctionCallCollector(self.entity_id_generator, self.model)

        # Assert
        expected_thread = Thread(thread.name)
        self.model.threads.add.assert_called_with(expected_thread)

    def test_on_call_it_ignores_it_if_the_function_is_unknown(self, threading):
        # Arrange
        frame_digest = fake('FrameDigest', spec_set=False)
        self.model.functions.get_by_id.side_effect = KeyError
        function_call_collector = FunctionCallCollector(self.entity_id_generator, self.model)

        # Act
        function_call = function_call_collector.on_call(frame_digest)

        # Assert
        assert_is_none(function_call)

    def test_it_relates_nested_function_calls(self, threading):
        # Arrange
        function_call_collector = FunctionCallCollector(self.entity_id_generator, self.model)

        # Act
        parent_function_call = function_call_collector.on_call(fake('FrameDigest'))
        child_function_call = function_call_collector.on_call(fake('FrameDigest'))

        # Assert
        assert_equal(child_function_call.parent, parent_function_call)

    def test_it_considers_returns_when_relating_nested_function_calls(self, threading):
        # Arrange
        function_call_collector = FunctionCallCollector(self.entity_id_generator, self.model)

        # Act
        function_call_collector.on_call(fake('FrameDigest'))
        child_function_call1 = function_call_collector.on_call(fake('FrameDigest'))
        function_call_collector.on_return(Mock())
        child_function_call2 = function_call_collector.on_call(fake('FrameDigest'))

        # Assert
        assert_equal(child_function_call1.parent, child_function_call2.parent)
