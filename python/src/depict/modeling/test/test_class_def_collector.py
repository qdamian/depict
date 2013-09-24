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

from depict.modeling.class_def_collector import ClassDefCollector
from mock import Mock, patch, call
from depict.model.class_ import Class_
import unittest

class TestClassDefCollector(unittest.TestCase):
    def test_creation(self):
        code_parser_mock = Mock()
        class_def_locator = ClassDefCollector(code_parser_mock, Mock())
        code_parser_mock.register.assert_called_once_with(class_def_locator)

    def test_registers_itself_in_source_code_parser(self):
        source_code_parser_mock = Mock()
        class_def_locator = ClassDefCollector(source_code_parser_mock, Mock())
        source_code_parser_mock.register.assert_called_once_with(class_def_locator)

    def test_adds_one_class_to_repo(self):
        with patch('depict.modeling.class_def_collector.global_module_repo') as module_repo_mock:
            with patch('depict.modeling.class_def_collector.global_class_repo') as class_repo_mock:
                entity_id_generator_mock = Mock()
                class_def_locator = ClassDefCollector(Mock(), entity_id_generator_mock)
                fake_node = Mock()
                fake_node.parent.file = 'path/to/file.py'
                fake_node.lineno = 27
                fake_node.name = 'fake_name'
                entity_id_generator_mock.create.return_value = 'to/file.py:27'

                class_def_locator.on_class(fake_node)

                expected_class = Class_('to/file.py:27', 'fake_name')
                class_repo_mock.add.assert_called_once_with(expected_class)

    def test_finds_module_to_init_the_class(self):
        with patch('depict.modeling.class_def_collector.global_class_repo') as class_repo_mock:
            with patch('depict.modeling.class_def_collector.global_module_repo') as module_repo_mock:
                source_code_parser_mock = Mock()
                entity_id_generator_mock = Mock()
                entity_id_generator_mock.create.return_value = 'path/to/file.py:27'
                source_code_parser_mock.base_path = '.'
                module_mock = Mock()
                module_repo_mock.get_by_id.return_value = module_mock
                class_def_locator = ClassDefCollector(source_code_parser_mock, entity_id_generator_mock)

                fake_node = Mock()
                fake_node.parent.file = 'path/to/file.py'
                fake_node.lineno = 27
                fake_node.name = 'fake_name'

                class_def_locator.on_class(fake_node)

                expected_class = Class_('path/to/file.py:27', 'fake_name', module_mock)
                class_repo_mock.add.assert_called_once_with(expected_class)
