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

from mock import Mock, sentinel, patch
from nose.tools import assert_is_instance

from depict.core.consolidation.data_source import DataSource
from depict.core.consolidation.util.handlers import QueueHandler
from depict.test.object_factory import real


class TestDataSource():
    @patch('depict.core.consolidation.data_source.EntityToJson')
    def test_it_logs_each_entity_of_the_data_model(self, entity_to_json):
        # Arrange
        data_source = DataSource(Queue.Queue())
        data_source.logger = Mock()
        data_source.entity_to_json = Mock()
        entity_to_json.convert.return_value = sentinel.serialized
        entity = real('Function')

        # Act
        data_source.on_entity(entity)

        # Assert
        entity_to_json.convert.assert_called_once_with(entity, 'id_')
        data_source.logger.warning.assert_called_once_with(sentinel.serialized)

    def test_each_log_entry_is_enqueued(self):
        # Arrange
        data_source = DataSource(Queue.Queue())
        entity = real('Function')

        # Act
        data_source.on_entity(entity)

        assert_is_instance(data_source.logger.handlers[0], QueueHandler)
