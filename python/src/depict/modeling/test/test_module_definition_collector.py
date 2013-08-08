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

from depict.model.module_repo import ModuleRepo
from depict.modeling.module_definition_collector import ModuleDefinitionCollector
from mock import Mock, patch, call
import unittest
from depict.model.module import Module

class TestModuleDefinitionCollector(unittest.TestCase):
    def test_creation(self):
        module_repo = ModuleRepo()
        code_parser_mock = Mock()
        module_def_collector = ModuleDefinitionCollector(
                                            code_parser_mock, module_repo)
        code_parser_mock.register.assert_called_once_with(module_def_collector)

    def test_registers_itself_in_source_code_parser(self):
        code_parser_mock = Mock()
        module_def_collector = ModuleDefinitionCollector(code_parser_mock, Mock())
        code_parser_mock.register.assert_called_once_with(module_def_collector)

    def test_adds_one_module_to_repo(self):
        with patch('depict.modeling.module_definition_collector.entity_id') as entity_id_mock:
            module_repo_mock = Mock()
            module_def_collector = ModuleDefinitionCollector(Mock(), module_repo_mock)
            fake_node = Mock()
            fake_node.file = 'path/to/file.py'
            fake_node.name = 'path.to.file'
            entity_id_mock.create.return_value = 'to/file.py'
            module_def_collector.on_module(fake_node)
            expected_module = Module('to/file.py', 'path.to.file')
            entity_id_mock.create.assert_called_once_with('path/to/file.py')
            module_repo_mock.add.assert_called_once_with(expected_module)

    def test_registers_dependency_with_other_modules_due_to_import(self):
        with patch('depict.modeling.module_definition_collector.Module') as module_class_mock:
            module_repo_mock = Mock()
            module_definition_collector = ModuleDefinitionCollector(Mock(), module_repo_mock)
            module_mock = Mock()
            module_class_mock.return_value = module_mock
            module_definition_collector.on_module(Mock(file='dummy/path/to/file.py'))
            fake_import = Mock()
            fake_import.names = [('some.module', None), ('some.other.module', None)]
            dependency1 = Mock()
            dependency2 = Mock()
            module_repo_mock.get_by_name.side_effect = lambda name: {
                                                        'some.module': dependency1,
                                                        'some.other.module': dependency2}[name]
            module_definition_collector.on_import(fake_import)
            module_mock.depends_on.assert_has_calls([call(dependency1), call(dependency2)])