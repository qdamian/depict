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

from depict.modeling.module_def_collector import ModuleDefCollector
from mock import Mock, call
import unittest
from depict.model.entity.module import Module

class TestModuleDefCollector(unittest.TestCase):
    def test_creation(self):
        code_parser_mock = Mock()
        module_def_collector = ModuleDefCollector(code_parser_mock, Mock(), Mock())
        code_parser_mock.register.assert_called_once_with(module_def_collector)

    def test_registers_itself_in_source_code_parser(self):
        code_parser_mock = Mock()
        module_def_collector = ModuleDefCollector(code_parser_mock, Mock(), Mock())
        code_parser_mock.register.assert_called_once_with(module_def_collector)

    def test_adds_one_module_to_repo(self):
        entity_id_generator_mock = Mock()
        model_mock = Mock()
        add_mock = Mock()
        model_mock.modules.add = add_mock
        module_def_collector = ModuleDefCollector(Mock(), entity_id_generator_mock, model_mock)
        fake_node = Mock()
        fake_node.file = 'path/to/file.py'
        fake_node.name = 'path.to.file'
        entity_id_generator_mock.create.return_value = 'to/file.py'

        module_def_collector.on_module(fake_node)

        expected_module = Module('to/file.py', 'path.to.file')
        entity_id_generator_mock.create.assert_called_once_with('path/to/file.py')

        add_mock.assert_called_once_with(expected_module)

class TestDependencyCollection():
    def setUp(self):
        self.model_mock = Mock()
        self.module_def_collector = ModuleDefCollector(Mock(), Mock(), self.model_mock)

        self.fake_importer = Mock()
        self.fake_importer.name = 'importer'

        self.importer_module_mock = Mock()
        self.dependency1 = Mock()
        self.dependency2 = Mock()
        self.model_mock.modules.get_by_name.side_effect = lambda name: {
                                                    'importer': self.importer_module_mock,
                                                    'some.module': self.dependency1,
                                                    'some.other.module': self.dependency2}[name]

    def test_registers_dependency_with_other_modules_due_to_import(self):
        # Arrange: emulate 'import some.module, some.other.module'
        fake_import_node = Mock()
        fake_import_node.names = [('some.module', None),
                             ('some.other.module', None)]

        # Act
        self.module_def_collector.on_import(self.fake_importer, fake_import_node)

        # Assert
        self.importer_module_mock.depends_on.assert_has_calls([call(self.dependency1), call(self.dependency2)])

    def test_registers_dependency_with_other_module_due_to_from_import(self):
        # Arrange: emulate 'from some.module import x'
        fake_from_node = Mock()
        fake_from_node.modname = 'some.module'

        # Act
        self.module_def_collector.on_from(self.fake_importer, fake_from_node)

        # Assert
        self.importer_module_mock.depends_on.assert_called_once_with(self.dependency1)
