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
from depict.model.class_repo import GlobalClassRepo
from depict.collection.static.source_code_parser import GlobalSourceCodeParser
from depict.model.module_repo import GlobalModuleRepo
from depict.model import entity_id

# pylint: disable=R0903
class ClassDefinitionCollector():
    def __init__(self, source_code_parser = GlobalSourceCodeParser,
                 class_repo = GlobalClassRepo):
        source_code_parser.register(self)
        self.class_repo = class_repo

    def on_class(self, node):
        module = GlobalModuleRepo.get(entity_id.create(node.parent.file))
        class_ = Class_(entity_id.create(node.parent.file, node.lineno),
                        node.name, module)
        self.class_repo.add(class_)