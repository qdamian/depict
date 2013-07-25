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

from depict.processing.function_definition_locator import FunctionDefinitionLocator
from depict.model.function_repo import FunctionRepo
from mock import Mock, create_autospec
from depict.model.function import Function
import unittest
from depict.model.class_ import Class_
from depict.model.class_repo import GlobalClassRepo
from depict.model.method import Method

class TestFunctionDefinitionLocator(unittest.TestCase):
    
    def test_creation(self):
        Functionrepo_ = FunctionRepo()
        code_parser_mock = Mock()
        class_def_locator = FunctionDefinitionLocator(code_parser_mock,
                                                   Functionrepo_)
        code_parser_mock.register.assert_called_once_with(class_def_locator)

    def test_register_itself_with_source_code_parser(self):
        code_parser_mock = Mock()
        class_def_locator = FunctionDefinitionLocator(code_parser_mock, Mock())
        code_parser_mock.register.assert_called_once_with(class_def_locator)

    def test_one_function_is_added_to_function_repo(self):
        function_repo_mock = Mock()
        function_definition_locator = FunctionDefinitionLocator(Mock(),
                                                                function_repo_mock)
        function_definition_locator.on_function('fake_function_name',
                                                'fake_function_id', None)
        expected_function = Function('fake_function_name', 'fake_function_id')
        function_repo_mock.add.assert_called_once_with(expected_function)

    def test_one_method_is_added_to_function_repo(self):
        function_repo_mock = Mock()
        function_definition_locator = FunctionDefinitionLocator(Mock(),
                                                                function_repo_mock)
        class_mock = create_autospec(Class_)
        class_mock.id_ = 'fake_class_id'
        GlobalClassRepo.add(class_mock)

        function_definition_locator.on_function('fake_function_name',
                                                'fake_function_id',
                                                class_mock.id_)
        expected_function = Function('fake_function_name', 'fake_function_id')
        function_repo_mock.add.assert_called_once_with(expected_function)
