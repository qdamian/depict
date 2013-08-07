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

from depict.collection.dynamic.thread_scoped_tracer import ThreadScopedTracer
from depict.modeling.class_definition_collector import \
                                                        ClassDefinitionCollector
from depict.modeling.function_definition_collector import \
                                                     FunctionDefinitionCollector
from depict.model.function_call import FunctionCall
from depict.modeling.definition_collection_orchestrator import \
                                          GlobalDefinitionCollectionOrchestrator

class FunctionCallNotifier():
    def __init__(self, observer):
        self.thread_scoped_tracer = ThreadScopedTracer(self)
        self.observer = observer
        GlobalDefinitionCollectionOrchestrator.include(ClassDefinitionCollector)
        GlobalDefinitionCollectionOrchestrator.include(
                                                    FunctionDefinitionCollector)
        self.stop = self.thread_scoped_tracer.stop

    def start(self):
        self.thread_scoped_tracer.start()

    def on_call(self, frame_digest):
        function_id = (frame_digest.file_name + ':' +
                       str(frame_digest.line_number))
        GlobalDefinitionCollectionOrchestrator.process(frame_digest.file_name)
        self.observer.on_call(FunctionCall(function_id))
