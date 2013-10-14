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

from mock import Mock, ANY

from depict.test.object_factory import fake, real
from depict.core.consolidation.data_sink import DataSink
from depict.core.consolidation.data_source import DataSource

class TestDataSink():
    def test_it_handles_one_entry(self):
        # Arrange
        data_source = DataSource()
        entity = real('Function')
        handler = Mock()
        data_sink = DataSink(handler)
        data_sink.start()

        # Act
        data_source.on_entity(entity)

        # Assert
        data_sink.stop()
        handler.handle.assert_any_call(entity)