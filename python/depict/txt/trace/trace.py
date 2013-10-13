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

from depict.core.model.util.entity_id_generator import EntityIdGenerator
from depict.core.modeling.dynamic.driver import Driver \
                                                as DynamicModelingDriver
from depict.core.consolidation.data_source import DataSource
from depict.core.consolidation.observable_model import ObservableModel
from depict.core.modeling.orchestrator import Orchestrator


class Trace(object):
    '''
    Trace representation.
    '''
    def __init__(self, base_path):
        data_source = DataSource()
        self.model = ObservableModel(data_source)
        self.logger = logging.getLogger(__name__)
        entity_id_generator = EntityIdGenerator(base_path)
        modeling_orchestrator = Orchestrator(base_path, self.model)
        self.function_call_notifier = DynamicModelingDriver(self,
                                                     entity_id_generator,
                                                     modeling_orchestrator)
        self.stop = self.function_call_notifier.stop

    def on_call(self, function_call):
        function_name = function_call.function.name
        actor_name = function_call.function.parent.name
        self.output(msg=function_name, actor=actor_name)

    def output(self, msg, actor):
        self.logger.debug('%s.%s' % (actor, msg))

    def start(self):
        self.function_call_notifier.start()