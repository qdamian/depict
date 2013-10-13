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

from depict.model.util.entity_id_generator import EntityIdGenerator
from depict.modeling.def_collection_orchestrator import DefCollectionOrchestator
from depict.modeling.function_call_notifier import FunctionCallNotifier
from depict.output.model_publisher import ModelPublisher
from depict.output.observable_model import ObservableModel


class TraceRepr(object):

    def __init__(self, base_path):
        publisher = ModelPublisher()
        self.model = ObservableModel(publisher)
        self.logger = logging.getLogger(__name__)
        entity_id_generator = EntityIdGenerator(base_path)
        def_collection_orchestrator = DefCollectionOrchestator(base_path,
                                                               self.model)
        self.function_call_notifier = FunctionCallNotifier(self,
                                            entity_id_generator,
                                            def_collection_orchestrator)
        self.stop = self.function_call_notifier.stop

    def on_call(self, function_call):
        function_name = function_call.function.name
        actor_name = function_call.function.parent.name
        self.output(msg=function_name, actor=actor_name)

    def output(self, msg, actor):
        self.logger.debug('%s.%s' % (actor, msg))

    def start(self):
        self.function_call_notifier.start()