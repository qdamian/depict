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
import time

from depict.core.modeling.orchestrator import Orchestrator
from depict.core.model.util.entity_id_generator import EntityIdGenerator
from depict.core.consolidation.data_sink import JsonDataSink
from depict.core.consolidation.observable_model import ObservableModel
from depict.core.consolidation.data_source import DataSource
from depict.core.modeling.dynamic.driver import Driver as DynamicModelingDriver
from depict.core.publishing.web_server import WebServer


class SequenceDiagram(object):
    def __init__(self, base_path):
        queue = Queue.Queue()
        data_source = DataSource(queue)
        self.model = ObservableModel(data_source)
        self.web_server = WebServer()
        self.data_sink = JsonDataSink(queue, self.web_server)

        entity_id_generator = EntityIdGenerator(base_path)
        modeling_orchestrator = Orchestrator(base_path, self.model)
        self.dynamic_modeling_driver = DynamicModelingDriver(self,
                                                        entity_id_generator,
                                                        modeling_orchestrator)

    def start(self):
        self.web_server.start()
        self.data_sink.start()
        self.dynamic_modeling_driver.start()

    def wait(self):
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            pass

    def stop(self):
        self.dynamic_modeling_driver.stop()
        self.data_sink.stop()
