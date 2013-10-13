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
from depict.core.modeling.static.function import Function as FunctionModeler
from depict.core.model.entity.method import Method
from depict.core.model.util.entity_id_generator import EntityIdGenerator
from depict.test.object_factory import fake, real
from mock import Mock, MagicMock
import astroid

class TestFunction():
    def setUp(self):
        self.source_code_parser = fake('SourceCodeParser')
        self.entity_id_generator = fake('EntityIdGenerator')
        self.model = fake('Model')
        self.function_modeler = FunctionModeler(self.source_code_parser,
                                                self.entity_id_generator,
                                                self.model)

    def test_it_registers_itself_with_source_code_parser(self):
        # Arranged and acted in setUp
        # Assert
        self.source_code_parser.register.assert_called_once_with(self.function_modeler)

    def test_one_function_is_added_to_function_repo(self):
        # Arrange
        module = real('Module')
        module.id_ = 'fake_file_name'
        self.model.modules.add(module)

        function_modeler = FunctionModeler(self.source_code_parser, EntityIdGenerator('.'), self.model)
        node = MagicMock()
        node.parent = Mock(spec=astroid.scoped_nodes.Module)
        node.parent.file = 'fake_file_name'
        node.lineno = 44

        # Act
        function_modeler.on_function(node)

        # Assert
        expected_function = Function('fake_file_name:44',
                                     'fake_function_name',
                                     module)
        self.model.functions.add.assert_called_once_with(expected_function)

    def test_one_method_is_added_to_function_repo(self):
        # Arrange
        class_mock = real('Class_')
        class_mock.id_ = 'fake_file_name:33'
        self.model.classes.add(class_mock)

        function_modeler = FunctionModeler(self.source_code_parser,
                                                 EntityIdGenerator('.'),
                                                 self.model)
        node = MagicMock()
        node.parent = Mock(spec=astroid.scoped_nodes.Class)
        node.parent.parent.file = 'fake_file_name'
        node.parent.lineno = 33
        node.name = 'fake_function_name'
        node.lineno = 44

        # Act
        function_modeler.on_function(node)

        # Assert
        expected_function = Method('fake_file_name:44',
                                   'fake_function_name',
                                   class_mock)
        self.model.functions.add.assert_called_once_with(expected_function)
