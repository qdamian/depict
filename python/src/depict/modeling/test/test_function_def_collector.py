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

from depict.model.class_ import Class_
from depict.model.function import Function
from depict.model.method import Method
from depict.modeling.function_def_collector import FunctionDefCollector
from mock import Mock, create_autospec, patch
import logilab
import unittest
from depict.model.util.entity_id_generator import EntityIdGenerator

class TestFunctionDefCollector(unittest.TestCase):

    def test_creation(self):
        code_parser_mock = Mock()
        class_def_locator = FunctionDefCollector(code_parser_mock, Mock())
        code_parser_mock.register.assert_called_once_with(class_def_locator)

    def test_register_itself_with_source_code_parser(self):
        source_code_parser_mock = Mock()
        class_def_locator = FunctionDefCollector(source_code_parser_mock, Mock())
        source_code_parser_mock.register.assert_called_once_with(class_def_locator)

    def test_one_function_is_added_to_function_repo(self):
        with patch('depict.modeling.function_def_collector.global_function_repo') as function_repo_mock:
            source_code_parser_mock = Mock()
            entity_id_generator_mock = Mock()
            entity_id_generator_mock.create.return_value = 'fake_file_name.py:44'
            function_def_collector = FunctionDefCollector(source_code_parser_mock,
                                                                 entity_id_generator_mock)
            fake_node = Mock()
            fake_node.parent.file = 'fake_file_name.py'
            fake_node.name = 'fake_function_name'
            fake_node.lineno = 44

            function_def_collector.on_function(fake_node)

            expected_function = Function('fake_file_name.py:44', 'fake_function_name')
            function_repo_mock.add.assert_called_once_with(expected_function)

    @patch('depict.modeling.function_def_collector.global_class_repo')
    @patch('depict.modeling.function_def_collector.global_function_repo')
    def test_one_method_is_added_to_function_repo(self, function_repo_mock, class_repo_mock):
                class_mock = create_autospec(Class_)
                class_mock.id_ = 'fake_file_name:33'
                class_repo_mock.add(class_mock)
                entity_id_generator = EntityIdGenerator('.')

                function_def_collector = FunctionDefCollector(Mock(), entity_id_generator)
                fake_node = Mock()
                fake_node.parent = Mock(spec=logilab.astng.scoped_nodes.Class)
                fake_node.parent.parent.file = 'fake_file_name'
                fake_node.parent.lineno = 33
                fake_node.name = 'fake_function_name'
                fake_node.lineno = 44

                function_def_collector.on_function(fake_node)

                expected_function = Method('fake_file_name:44',
                                           'fake_function_name',
                                           class_mock)
                function_repo_mock.add.assert_called_once_with(expected_function)
