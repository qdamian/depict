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

from depict.modeling.module_def_collector import ModuleDefCollector
from mock import Mock, patch, call
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
        # FIXME
        # add_mock.assert_called_once_with(expected_module)

class TestDependencyCollection():
    def setUp(self):
        self.module_class_patcher = patch('depict.modeling.module_def_collector.Module')
        module_class_mock = self.module_class_patcher.start()
        source_code_parser_mock = Mock()
        self.model_mock = Mock()
        self.module_def_collector = ModuleDefCollector(source_code_parser_mock, Mock(), self.model_mock)
        self.module_mock = Mock()
        module_class_mock.return_value = self.module_mock
        self.module_def_collector.on_module(Mock(file='dummy/path/to/file.py'))

    def tearDown(self):
        self.module_class_patcher.stop()

    def test_registers_dependency_with_other_modules_due_to_import(self):
        dependency1 = Mock()
        dependency2 = Mock()
        self.model_mock.modules.get_by_name.side_effect = lambda name: {
                                                    'some.module': dependency1,
                                                    'some.other.module': dependency2}[name]
        fake_import = Mock()
        fake_import.names = [('some.module', None), ('some.other.module', None)]
        self.module_def_collector.on_import(fake_import)
        self.module_mock.depends_on.assert_has_calls([call(dependency1), call(dependency2)])

    def test_registers_dependency_with_other_module_due_to_from_import(self):
        dependency = Mock()
        self.model_mock.modules.get_by_name.side_effect = lambda name: {'some.module': dependency }[name]
        fake_import = Mock()
        fake_import.modname = 'some.module'
        module_mock = Mock()
        self.module_def_collector.current_module = module_mock

        self.module_def_collector.on_from(fake_import)

        module_mock.depends_on.assert_called_once_with(dependency)
