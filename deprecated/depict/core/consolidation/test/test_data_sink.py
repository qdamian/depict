#region GPLv3 notice
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
#endregion

import Queue
from mock import Mock
from nose.tools import *

from depict.test.object_factory import real
from depict.core.consolidation.data_sink import EntityDataSink
from depict.core.consolidation.data_source import DataSource

class TestEntityDataSink():
    def setUp(self):
        queue = Queue.Queue()
        self.data_source = DataSource(queue)
        self.handler = Mock()
        self.data_sink = EntityDataSink(queue, self.handler)
        self.data_sink.start()

    def test_it_handles_one_entry(self):
        # Arrange
        entity = real('Thread')

        # Act
        self.data_source.on_entity(entity)

        # Assert
        self.data_sink.stop()
        self.handler.handle.assert_any_call(entity)
        assert_equal(self.handler.handle.call_count, 1)

    def test_it_(self):
        # Arrange
        module = real('Module')
        function = real('Function')

        # Act
        self.data_source.on_entity(function)
        self.data_source.on_entity(module)
        self.data_source.on_entity(function)

        # Assert
        self.data_sink.stop()
        assert_equal(self.handler.handle.call_count, 2)

    # TO DO: Test references

    # TO DO: Test missing references
