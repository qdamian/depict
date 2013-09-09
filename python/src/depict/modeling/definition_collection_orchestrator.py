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

from depict.collection.static.source_code_parser import GlobalSourceCodeParser

class DefinitionCollectionOrchestrator(object):
    def __init__(self):
        self.collectors = []
        self.source_code_parser = GlobalSourceCodeParser

    def include(self, collector):
        self.collectors.append(collector)

    def process(self, file_paths):
        for collector in self.collectors:
            collector()
        self.source_code_parser.add_files(file_paths)
        self.source_code_parser.parse()

    def set_base_path(self, base_path):
        self.source_code_parser.set_base_path(base_path)

# pylint: disable=C0103
GlobalDefinitionCollectionOrchestrator = DefinitionCollectionOrchestrator()
