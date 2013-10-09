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

from depict.model.entity.function_call import FunctionCall
from depict.model.entity.thread import Thread
import threading
import time
import uuid

class FunctionCallCollector(object):

    def __init__(self, entity_id_generator, model):
        self.entity_id_generator = entity_id_generator
        self.model = model

        current_thread = Thread(threading.current_thread().name)
        self.model.threads.add(current_thread)
        self.current_function = current_thread

    def on_call(self, frame_digest):
        function = self._identify_function(frame_digest)
        if not function:
            return
        function_call_id = '%s@%s-%s' % (function.id_,
                                         time.time(),
                                         uuid.uuid4())
        function_call = FunctionCall(function_call_id, function,
                                     self.current_function)
        self.current_function = function_call
        self.model.function_calls.add(function_call)
        return function_call

    # pylint:disable = unused-argument
    def on_return(self, frame_digest):
        self.current_function = self.current_function.parent

    def _identify_function(self, frame_digest):
        function_id = self.entity_id_generator.create(frame_digest.file_name,
                                                      frame_digest.line_number)
        try:
            return self.model.functions.get_by_id(function_id)
        except KeyError:
            return None