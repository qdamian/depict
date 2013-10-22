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

import logging
from depict.core.consolidation.util.entity_to_json import EntityToJson
from depict.core.consolidation.util.handlers import QueueHandler


class DataSource(object):
    def __init__(self, queue):
        self.logger = logging.getLogger(__name__)
        # Higher level loggers could write to console
        self.logger.propagate = False

        queue_handler = QueueHandler(queue)
        self.logger.addHandler(queue_handler)

    def on_entity(self, entity):
        self.logger.warning(EntityToJson.convert(entity, 'id_'))
