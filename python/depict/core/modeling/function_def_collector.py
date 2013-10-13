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

from depict.core.model.entity.function import Function
from depict.core.model.entity.method import Method
import astroid

class FunctionDefCollector(object):
    '''
    Create an entity in the model for each function definition, converting
    nodes from the Astroid representation to depict's representation.
    '''

    def __init__(self, source_code_parser, entity_id_gen, model):
        self.entity_id_gen = entity_id_gen
        self.model = model
        source_code_parser.register(self)

    def on_function(self, node):
        if isinstance(node.parent, astroid.scoped_nodes.Class):
            function = self._create_method_entity(node)
        else:
            function = self._create_function_entity(node)
        self.model.functions.add(function)

    def _create_method_entity(self, node):
        id_ = self.entity_id_gen.create(node.parent.parent.file, node.lineno)
        class_id = self.entity_id_gen.create(node.parent.parent.file,
                                             node.parent.lineno)
        class_ = self.model.classes.get_by_id(class_id)
        function = Method(id_, node.name, class_)
        class_.add_method(function)
        return function

    def _create_function_entity(self, node):
        id_ = self.entity_id_gen.create(node.parent.file, node.lineno)
        module_id = self.entity_id_gen.create(node.parent.file)
        module = self.model.modules.get_by_id(module_id)
        return Function(id_, node.name, module)
