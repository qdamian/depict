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
from depict.model import entity_id
from depict.model.module import Module
from depict.model.module_repo import GlobalModuleRepo

# pylint: disable=R0903
class ModuleDefinitionCollector(object):
    def __init__(self, source_code_parser = GlobalSourceCodeParser,
                 module_repo = GlobalModuleRepo):
        source_code_parser.register(self)
        self.module_repo = module_repo
        self.current_module = None

    def on_module(self, node):
        self.current_module = Module(entity_id.create(node.file), node.name)
        self.module_repo.add(self.current_module)

    def on_import(self, node):
        for module_name in node.names:
            module = self.module_repo.get_by_name(module_name[0])
            if module:
                self.current_module.depends_on(module)

    def on_from(self, node):
        module = self.module_repo.get_by_name(node.modname)
        if module:
            self.current_module.depends_on(module)