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

import Queue
from depict.core.consolidation.util import json_to_entity
from depict.core.consolidation.util.handlers import QueueListener
from depict.core.model.entity.thread import Thread


class DataSink(object):
    queue = Queue.Queue()

    def __init__(self, handler):
        self.queue_listener = None
        self.handler = handler

    def start(self):
        self.queue_listener = QueueListener(DataSink.queue, self)
        self.queue_listener.start()

    def stop(self):
        if self.queue_listener:
            self.queue_listener.stop()

    def handle(self, log_entry):
        entity = json_to_entity.convert(log_entry.msg)
        self.handler.handle(entity)
