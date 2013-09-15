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

from depict.model.class_ import Class_
from depict.model.util.module_repo import global_module_repo
from depict.model.util.class_repo import global_class_repo

# pylint:disable = too-few-public-methods
class ClassDefinitionCollector(object):
    def __init__(self, source_code_parser, entity_id_gen):
        self.entity_id_gen = entity_id_gen
        source_code_parser.register(self)

    def on_class(self, node):
        module_id = self.entity_id_gen.create(node.parent.file)
        module = global_module_repo.get_by_id(module_id)
        id_ = self.entity_id_gen.create(node.parent.file,
                               node.lineno)
        class_ = Class_(id_, node.name, module)
        global_class_repo.add(class_)