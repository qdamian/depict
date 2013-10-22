#region GPLv3 notice
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
#endregion

from depict.core.model.entity.module import Module as ModuleEntity

class Module(object):
    def __init__(self, source_code_parser, entity_id_generator, model):
        self.source_code_parser = source_code_parser
        self.entity_id_generator = entity_id_generator
        self.model = model
        source_code_parser.register(self)

    def on_module(self, node):
        module_id = self.entity_id_generator.create(node.file)
        self.model.modules.add(ModuleEntity(module_id, node.name))

    def on_import(self, parent_node, node):
        for module_name in node.names:
            self._assign_dependency(parent_node.name, module_name[0])

    def on_from(self, parent_node, node):
        self._assign_dependency(parent_node.name, node.modname)

    def _assign_dependency(self, importer_name, imported_name):
        try:
            importer = self.model.modules.get_by_name(importer_name)
            imported = self.model.modules.get_by_name(imported_name)
            importer.depends_on(imported)
        except KeyError:
            pass
