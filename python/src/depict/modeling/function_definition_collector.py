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
from depict.model.class_repo import GlobalClassRepo
from depict.model.function_repo import GlobalFunctionRepo
from depict.collection.static.source_code_parser import GlobalSourceCodeParser
from depict.model import entity_id
from logilab import astng

# pylint: disable=R0903
class FunctionDefinitionCollector(object):
    def __init__(self, source_code_parser = GlobalSourceCodeParser,
                 function_repo = GlobalFunctionRepo):
        source_code_parser.register(self)
        self.function_repo = function_repo

    def on_function(self, node):
        name = node.name
        if isinstance(node.parent, astng.scoped_nodes.Class):
            id_ = entity_id.create(node.parent.parent.file, node.lineno)
            class_id = entity_id.create(node.parent.parent.file,
                                        node.parent.lineno)
            class_ = GlobalClassRepo.get_by_id(class_id)
            function = Method(id_, name, class_)
            class_.add_method(function)
        else:
            id_ = entity_id.create(node.parent.file, node.lineno)
            function = Function(id_, name)
        self.function_repo.add(function)