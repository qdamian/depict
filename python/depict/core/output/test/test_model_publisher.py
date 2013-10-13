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

from mock import patch

from depict.core.output.model_publisher import ModelPublisher
from depict.test.template import real


class TestModelPublisher():

    @patch('depict.core.output.model_publisher.LOGGER')
    def test_it_logs_each_entity(self, logger):
        model_publisher = ModelPublisher()
        entity = real('Function')
        model_publisher.on_entity(entity)
        logger.info.assert_called_once_with(entity)
