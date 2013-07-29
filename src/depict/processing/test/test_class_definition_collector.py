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

from depict.processing.class_definition_collector import ClassDefinitionCollector
from depict.model.class_repo import ClassRepo
from mock import Mock, patch
from depict.model.class_ import Class_
import unittest

class TestClassDefinitionCollector(unittest.TestCase):
    def test_creation(self):
        class_repo = ClassRepo()
        code_parser_mock = Mock()
        class_def_locator = ClassDefinitionCollector(code_parser_mock,
                                                   class_repo)
        code_parser_mock.register.assert_called_once_with(class_def_locator)

    def test_registers_itself_in_source_code_parser(self):
        code_parser_mock = Mock()
        class_def_locator = ClassDefinitionCollector(code_parser_mock, Mock())
        code_parser_mock.register.assert_called_once_with(class_def_locator)

    def test_adds_one_class_to_repo(self):
        class_repo = Mock()
        class_def_locator = ClassDefinitionCollector(Mock(), class_repo)
        class_def_locator.on_class('fake_id', 'fake_name', 'dummy_module_id')
        expected_class = Class_('fake_id', 'fake_name')
        class_repo.add.assert_called_once_with(expected_class)
        
    @patch('depict.processing.class_definition_collector.GlobalModuleRepo')
    def test_finds_module_to_init_the_class(self, module_repo_mock):
        fake_module = Mock()
        module_repo_mock.get.return_value = fake_module
        class_repo = Mock()
        class_def_locator = ClassDefinitionCollector(Mock(), class_repo)
        class_def_locator.on_class('fake_class_id', 'dummy_class_name', 'fake_module_id')
        module_repo_mock.get.assert_called_once_with('fake_module_id')
        expected_class = Class_('fake_class_id', 'dummy_class_name', fake_module)
        class_repo.add.assert_called_once_with(expected_class)