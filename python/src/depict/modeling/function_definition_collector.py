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

from depict.model.function import Function
from depict.model.method import Method
from logilab import astng
from depict.model.util.class_repo import global_class_repo
from depict.model.util.function_repo import global_function_repo

# pylint:disable = too-few-public-methods
class FunctionDefinitionCollector(object):
    def __init__(self, source_code_parser, entity_id_gen):
        self.entity_id_gen = entity_id_gen
        source_code_parser.register(self)

    def on_function(self, node):
        name = node.name
        if isinstance(node.parent, astng.scoped_nodes.Class):
            id_ = self.entity_id_gen.create(node.parent.parent.file,
                                            node.lineno)
            class_id = self.entity_id_gen.create(node.parent.parent.file,
                                                 node.parent.lineno)
            class_ = global_class_repo.get_by_id(class_id)
            function = Method(id_, name, class_)
            class_.add_method(function)
        else:
            id_ = self.entity_id_gen.create(node.parent.file, node.lineno)
            function = Function(id_, name)
        global_function_repo.add(function)