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

from depict.processing.class_definition_locator import ClassDefinitionLocator
from depict.model.class_repo import ClassRepo
from mock import Mock
from depict.model.class_ import Class_
import unittest

class TestClassDefinitionLocator(unittest.TestCase):
    def test_creation(self):
        class_repo = ClassRepo()
        code_parser_mock = Mock()
        class_def_locator = ClassDefinitionLocator(code_parser_mock,
                                                   class_repo)
        code_parser_mock.register.assert_called_once_with(class_def_locator)

    def test_adds_oneClass_to_repo(self):
        class_repo_mock = Mock()
        code_parser_mock = Mock()
        class_def_locator = ClassDefinitionLocator(code_parser_mock,
                                                   class_repo_mock)
        expected_class = Class_('fakeClass_name', 'fakeClass_id')
        code_parser_mock.parse.side_effect = (lambda a, b:
                                class_def_locator.on_class(expected_class.name,
                                                           expected_class.id_))
        class_def_locator.process('fake_file_name', 'fake_code') 
        code_parser_mock.parse.assert_called_once_with('fake_file_name',
                                                       'fake_code')
        (args, _) = class_repo_mock.add.call_args
        actual_class = args[0]
        self.assertEqual(actual_class.name, expected_class.name)
        self.assertEqual(actual_class.id_, expected_class.id_)
