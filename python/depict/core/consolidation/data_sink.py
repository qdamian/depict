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

from depict.core.consolidation.util.handlers import QueueListener
from depict.core.consolidation.util.json_to_entity import JsonToEntity


class JsonDataSink(object):
    def __init__(self, queue, handler):
        self.handler = handler
        self.queue = queue
        self.queue_listener = None

    def start(self):
        self.queue_listener = QueueListener(self.queue, self)
        self.queue_listener.start()

    def stop(self):
        if self.queue_listener:
            self.queue_listener.stop()

    def handle(self, log_entry):
        self.handler.handle(log_entry.msg)

class EntityDataSink(object):
    def __init__(self, queue, handler):
        self.handler = handler
        self.json_data_sink = JsonDataSink(queue, self)
        self.json_to_entity = JsonToEntity()

    def start(self):
        self.json_data_sink.start()

    def stop(self):
        self.json_data_sink.stop()

    def handle(self, json_serialized_entity):
        try:
            entity = self.json_to_entity.convert(json_serialized_entity)
            self.handler.handle(entity)
        except KeyError:
            pass
