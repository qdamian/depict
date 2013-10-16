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
from depict.core.model.entity.function_call import FunctionCall
from depict.core.model.entity.class_ import Class_
from depict.core.model.entity.module import Module
from depict.core.consolidation.data_sink import DataSink

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
        self.data_sink = DataSink(self)

        entity_id_generator = EntityIdGenerator(base_path)
        modeling_orchestrator = Orchestrator(base_path, self.model)
        self.dynamic_modeling_driver = DynamicModelingDriver(self,
                                                     entity_id_generator,
                                                     modeling_orchestrator)

    def handle(self, entity):
        if isinstance(entity, FunctionCall):
            module_name = 'depict.%s' % self._get_module_name(entity)
            function_name = entity.function.name
            actor_name = entity.function.parent.name
            self.output(module=module_name, msg=function_name, actor=actor_name)

    def output(self, module, msg, actor):
        logger = logging.getLogger(module)
        logger.info('%s.%s' % (actor, msg))

    def _get_module_name(self, function_call):
        parent = function_call.function.parent
        if isinstance(parent, Class_):
            return parent.module.name
        elif isinstance(parent, Module):
            return parent.name # Modules

    def start(self):
        self.data_sink.start()
        self.dynamic_modeling_driver.start()

    def stop(self):
        self.dynamic_modeling_driver.stop()
        self.data_sink.stop()
