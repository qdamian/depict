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
from depict.processing.module_definition_collector import ModuleDefinitionCollector
from mock import Mock
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
        module_repo = Mock()
        module_def_collector = ModuleDefinitionCollector(Mock(), module_repo)
        module_def_collector.on_module('fake_id', 'fake_name')
        expected_module = Module('fake_id', 'fake_name')
        module_repo.add.assert_called_once_with(expected_module)