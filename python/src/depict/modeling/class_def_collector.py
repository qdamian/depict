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

from depict.model.entity.class_ import Class_

# pylint:disable = too-few-public-methods
class ClassDefCollector(object):
    def __init__(self, source_code_parser, entity_id_gen, model):
        self.entity_id_gen = entity_id_gen
        self.model = model
        source_code_parser.register(self)

    def on_class(self, node):
        module_id = self.entity_id_gen.create(node.parent.file)
        module = self.model.modules.get_by_id(module_id)
        id_ = self.entity_id_gen.create(node.parent.file,
                               node.lineno)
        class_ = Class_(id_, node.name, module)
        self.model.classes.add(class_)