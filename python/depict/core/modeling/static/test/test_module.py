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

from mock import Mock, call

from depict.core.modeling.static.module import Module as ModuleModeler
from depict.core.model.entity.module import Module
from depict.test.object_factory import fake, real


class TestModule():
    def setUp(self):
        self.source_code_parser = fake('SourceCodeParser')
        self.entity_id_generator = fake('EntityIdGenerator')
        self.model = fake('Model')
        self.module_modeler = ModuleModeler(self.source_code_parser,
                                            self.entity_id_generator,
                                            self.model)

    def test_registers_itself_in_source_code_parser(self):
        # Arranged and acted on setUp
        # Assert
        self.source_code_parser.register.assert_called_once_with(self.module_modeler)

    def test_adds_one_module_to_the_model(self):
        # Arrange
        fake_node = fake('NodeNG', spec_set=False)
        fake_node.file = 'path/to/file.py'
        fake_node.name = 'path.to.file'
        self.entity_id_generator.create.return_value = 'to/file.py'

        # Act
        self.module_modeler.on_module(fake_node)

        # Assert
        expected_module = Module('to/file.py', 'path.to.file')
        self.entity_id_generator.create.assert_called_once_with('path/to/file.py')
        self.model.modules.add.assert_called_once_with(expected_module)

class TestDependencyModeling():
    def setUp(self):
        self.model = fake('Model')
        self.module_modeler = ModuleModeler(fake('SourceCodeParser'),
                                            fake('EntityIdGenerator'),
                                            self.model)

        self.fake_importer = real('Module')
        self.fake_importer.name = 'importer'

        self.importer_module = Mock()
        self.dependency1 = real('Module')
        self.dependency2 = real('Module')
        self.model.modules.get_by_name.side_effect = lambda name: {
                                                    'importer': self.importer_module,
                                                    'some.module': self.dependency1,
                                                    'some.other.module': self.dependency2}[name]

    def test_registers_dependency_with_other_modules_due_to_import(self):
        # Arrange: emulate 'import some.module, some.other.module'
        fake_import_node = fake('NodeNG', spec_set=False)
        fake_import_node.names = [('some.module', None),
                                  ('some.other.module', None)]

        # Act
        self.module_modeler.on_import(self.fake_importer, fake_import_node)

        # Assert
        self.importer_module.depends_on.assert_has_calls([call(self.dependency1), call(self.dependency2)])

    def test_registers_dependency_with_other_module_due_to_from_import(self):
        # Arrange: emulate 'from some.module import x'
        fake_from_node = fake('NodeNG', spec_set=False)
        fake_from_node.modname = 'some.module'

        # Act
        self.module_modeler.on_from(self.fake_importer, fake_from_node)

        # Assert
        self.importer_module.depends_on.assert_called_once_with(self.dependency1)
