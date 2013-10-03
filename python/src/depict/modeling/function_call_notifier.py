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

from depict.collection.dynamic.thread_scoped_tracer import ThreadScopedTracer
from depict.model.entity.function_call import FunctionCall
from depict.modeling.class_def_collector import ClassDefCollector
from depict.modeling.function_def_collector import FunctionDefCollector
from depict.modeling.module_def_collector import ModuleDefCollector
from depict.modeling.def_collection_orchestrator import AlreadyProcessed
import threading
from depict.model.entity.thread import Thread
import time
import uuid
from depict.model.util.entity_repo import EntityRepo

class FunctionCallNotifier(object):
    def __init__(self, observer, entity_id_generator,
                 def_collection_orchestrator):
        self.observer = observer
        self.entity_id_generator = entity_id_generator
        self.def_collection_orchestrator = def_collection_orchestrator

        self._add_dependencies()

        self.thread_scoped_tracer = ThreadScopedTracer(self)
        self.stop = self.thread_scoped_tracer.stop

        current_thread = Thread(threading.current_thread().name)
        thread_repo = EntityRepo()
        thread_repo.add(current_thread)
        self.current_function = current_thread

    def start(self):
        self.thread_scoped_tracer.start()

    def on_call(self, frame_digest):

        if frame_digest.function_name == '<module>':
            return

        function_id = self.entity_id_generator.create(frame_digest.file_name,
                                                      frame_digest.line_number)
        function_call_id = '%s@%s-%s' % (function_id, time.time(), uuid.uuid4())
        self._collect_defs_if_needed(frame_digest.file_name)
        function_call = FunctionCall(function_call_id, function_id,
                                     self.current_function,
                                     self.def_collection_orchestrator.model)
        self.observer.on_call(function_call)
        self.current_function = function_call

    # pylint:disable = unused-argument
    def on_return(self, frame_digest):
        self.current_function = self.current_function.parent

    def _add_dependencies(self):
        self.def_collection_orchestrator.include(ModuleDefCollector)
        self.def_collection_orchestrator.include(ClassDefCollector)
        self.def_collection_orchestrator.include(FunctionDefCollector)

    def _collect_defs_if_needed(self, file_name):
        try:
            self.def_collection_orchestrator.process(file_name)
        except AlreadyProcessed:
            pass
