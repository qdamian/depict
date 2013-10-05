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

from depict.modeling.class_def_collector import ClassDefCollector
from depict.model.entity.class_ import Class_
from depict.test.template import fake

class TestClassDefCollector():
    def setUp(self):
        self.source_code_parser = fake('SourceCodeParser')
        self.entity_id_generator = fake('EntityIdGenerator')
        self.model = fake('Model')
        self.class_def_locator = ClassDefCollector(self.source_code_parser,
                                                   self.entity_id_generator,
                                                   self.model)

    def test_it_registers_itself_with_the_source_code_parser_on_creation(self):
        # Arranged and acted on setUp

        # Assert
        self.source_code_parser.register.assert_called_once_with(
                                                        self.class_def_locator)

    def test_it_adds_one_class_to_repo(self):
        # Arrange
        node = fake('NodeNG', spec_set=False)
        node.parent.file = 'path/to/file.py'
        node.lineno = 27
        node.name = 'fake_class_name'
        self.entity_id_generator.create.return_value = 'to/file.py:27'

        # Act
        self.class_def_locator.on_class(node)

        # Assert
        expected_class = Class_('to/file.py:27', 'fake_class_name')
        self.model.classes.add.assert_called_once_with(expected_class)

    def test_it_initializes_the_classes_with_the_module_they_belong_to(self):
        # Arrange
        self.entity_id_generator.create.return_value = 'path/to/file.py:27'
        module = fake('Module')
        self.model.modules.get_by_id.return_value = module
        node = fake('NodeNG', spec_set=False)
        node.parent.file = 'path/to/file.py'
        node.lineno = 27
        node.name = 'fake_class_name'

        # Act
        self.class_def_locator.on_class(node)

        # Assert
        expected_class = Class_('path/to/file.py:27', 'fake_class_name', module)
        self.model.classes.add.assert_called_once_with(expected_class)
