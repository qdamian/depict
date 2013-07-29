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

from mock import Mock, MagicMock, call, ANY, patch, mock_open, PropertyMock
from depict.presentation.toy.definition_list import DefinitionList
from depict.collection.dynamic.frame_digest import FrameDigest
from depict.model.function_call import FunctionCall
from depict.model.function import Function
import unittest
from depict.model.class_ import Class_

@patch('depict.presentation.toy.definition_list.open', create=True)
class TestDefinitionList(unittest.TestCase):
    def test_init_opens_output_file(self, open_mock):
        DefinitionList('dummy_input_glob', 'mock_output_file_name')
        open_mock.assert_called_once_with('mock_output_file_name', 'w')

    def test_init_finds_files_in_input_directory(self, open_mock):
        with patch('depict.presentation.toy.definition_list.FileSet') as fileset_mock:
            fake_include_glob = 'path/to/**/files*.py'
            DefinitionList(fake_include_glob, 'dummy_out_filename')
            fileset_mock.assert_called_once_with(fake_include_glob)

    def test_init_creates_static_data_notifier(self, open_mock):
        with patch('depict.presentation.toy.definition_list.StaticDataNotifier') as static_data_notifier_mock:
            with patch('depict.presentation.toy.definition_list.FileSet') as fileset_class_mock:
                expected_paths = ['fake/file/a.py', 'file/file/b.py']
                fileset_mock = MagicMock()
                fileset_mock.__iter__.return_value = expected_paths
                fileset_class_mock.return_value = fileset_mock
                definition_list = DefinitionList('dummy_input_glob', 'dummy_filename')
                static_data_notifier_mock.assert_called_once_with(expected_paths, definition_list)
 
    def test_runs_static_definition_notifier(self, open_mock):
        definition_list = DefinitionList('dummy_input_glob', 'dummy_filename')
        definition_list.static_data_notifier = Mock()
        definition_list.run()
        definition_list.static_data_notifier.run.assert_called_once_with()

    def test_stores_function_name_for_each_function(self, open_mock):
        file_mock = Mock()
        open_mock.return_value = file_mock
        definition_list = DefinitionList('dummy_input_glob', 'dummy_filename')
        fake_function = Function('fake_id', 'fake_name')
        definition_list.on_function(fake_function)
        expected_call = call('fake_name\n')
        self.assertTrue(expected_call in file_mock.write.mock_calls)

    def test_stores_class_name_for_each_class(self, open_mock):
        file_mock = Mock()
        open_mock.return_value = file_mock
        definition_list = DefinitionList('dummy_input_glob', 'dummy_filename')
        fake_class = Class_('fake_id', 'fake_name')
        definition_list.on_class(fake_class)
        expected_call = call('fake_name\n')
        self.assertTrue(expected_call in file_mock.write.mock_calls)
