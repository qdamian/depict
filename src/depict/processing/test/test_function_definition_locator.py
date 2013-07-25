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

    def test_one_function_is_added_to_function_repo(self):
        function_repo_mock = Mock()
        code_parser_mock = Mock()
        class_def_locator = FunctionDefinitionLocator(code_parser_mock,
                                                   function_repo_mock)
        expected_function = Function('dummy_function_name',
                                      'dummy_function_id')
        code_parser_mock.parse.side_effect = (lambda file_name, src_file:
                                class_def_locator.on_function(expected_function.name,
                                                           expected_function.id_,
                                                           None))
        class_def_locator.process('fake_file_name', 'fake_code') 
 
        code_parser_mock.parse.assert_called_once_with('fake_file_name', 'fake_code')
        function_repo_mock.add.assert_called_once_with(expected_function)
 
    def test_one_method_is_added_to_class(self):
        function_repo_mock = Mock()
        code_parser_mock = Mock()
        class_def_locator = FunctionDefinitionLocator(code_parser_mock,
                                                   function_repo_mock)
        class_mock = create_autospec(Class_)
        class_mock.id_ = 'fake_class_id'
        GlobalClassRepo.add(class_mock)
        expected_method = Method('fake_function_name', 'fake_function_id',
                                 class_mock.id_)
        code_parser_mock.parse.side_effect = (lambda file_name, src_file:
                                class_def_locator.on_function(expected_method.name,
                                                           expected_method.id_,
                                                           class_mock.id_))

        class_def_locator.process('fake_file_name', 'fake_code')

        class_mock.add_method.assert_called_once_with(expected_method)