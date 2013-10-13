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

from depict.collection.dynamic.project_modules_filter import \
                                                         ProjectModulesFilter
from depict.collection.dynamic.thread_scoped_tracer import ThreadScopedTracer
from depict.modeling.class_def_collector import ClassDefCollector
from depict.modeling.function_call_collector import FunctionCallCollector
from depict.modeling.function_def_collector import FunctionDefCollector
from depict.modeling.module_def_collector import ModuleDefCollector
from depict.modeling.def_collection_orchestrator import AlreadyProcessed

class FunctionCallNotifier(object):
    def __init__(self, observer, entity_id_generator,
                 def_collection_orchestrator):
        self.observer = observer
        self.def_collection_orchestrator = def_collection_orchestrator

        self.function_call_collector = FunctionCallCollector(
                                            entity_id_generator,
                                            def_collection_orchestrator.model)

        self._setup_static_data_collection()

        project_modules_filter = ProjectModulesFilter(
                                        entity_id_generator.base_path, self)
        self.thread_scoped_tracer = ThreadScopedTracer(project_modules_filter)
        self.stop = self.thread_scoped_tracer.stop

    def start(self):
        self.thread_scoped_tracer.start()

    def on_call(self, frame_digest):
        # I wonder what this is...
        if frame_digest.function_name == '<module>':
            return

        self._collect_defs_from(frame_digest.file_name)
        function_call = self.function_call_collector.on_call(frame_digest)
        self.observer.on_call(function_call)

    def _setup_static_data_collection(self):
        self.def_collection_orchestrator.include(ModuleDefCollector)
        self.def_collection_orchestrator.include(ClassDefCollector)
        self.def_collection_orchestrator.include(FunctionDefCollector)

    def _collect_defs_from(self, file_name):
        try:
            self.def_collection_orchestrator.process(file_name)
        except AlreadyProcessed:
            pass
