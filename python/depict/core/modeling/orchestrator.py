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

from depict.core.model.util.entity_id_generator import EntityIdGenerator
from depict.core.collection.static.source_code_parser import SourceCodeParser

class AlreadyProcessed(Exception):
    pass

class Orchestrator(object):
    def __init__(self, base_path, model):
        self.modelers = []
        self.model = model
        self.entity_id_generator = EntityIdGenerator(base_path)
        self.source_code_parser = SourceCodeParser(base_path)

    def include(self, modeler):
        self.modelers.append(modeler)

    def process(self, file_paths):
        assert file_paths
        if not self.source_code_parser.add_files(file_paths):
            raise AlreadyProcessed(file_paths)

        for modeler in self.modelers:
            modeler(self.source_code_parser,
                    self.entity_id_generator,
                    self.model)

        self.source_code_parser.parse()
