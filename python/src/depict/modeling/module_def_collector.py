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

from depict.model.module import Module
from depict.model.util.module_repo import global_module_repo

# pylint:disable = too-few-public-methods
class ModuleDefCollector(object):
    def __init__(self, source_code_parser, entity_id_generator):
        self.source_code_parser = source_code_parser
        self.entity_id_generator = entity_id_generator
        self.current_module = None
        source_code_parser.register(self)

    def on_module(self, node):
        module_id = self.entity_id_generator.create(node.file)
        self.current_module = Module(module_id, node.name)
        global_module_repo.add(self.current_module)

    def on_import(self, node):
        for module_name in node.names:
            try:
                module = global_module_repo.get_by_name(module_name[0])
                self.current_module.depends_on(module)
            except KeyError:
                pass

    def on_from(self, node):
        try:
            module = global_module_repo.get_by_name(node.modname)
            self.current_module.depends_on(module)
        except KeyError:
            pass