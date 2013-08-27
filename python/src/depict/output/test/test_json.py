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

from depict.output.json import Json
from mock import patch, MagicMock, Mock
import unittest

class TestJson(unittest.TestCase):

    def test_init_creates_static_data_notifier(self):
        with patch('depict.output.json.StaticDataNotifier') as static_data_notifier_mock:
            with patch('depict.output.json.FileSet') as fileset_class_mock:
                expected_paths = ['fake/file/a.py', 'file/file/b.py']
                fileset_mock = MagicMock()
                fileset_mock.__iter__.return_value = expected_paths
                fileset_class_mock.return_value = fileset_mock
                json = Json('dummy_input_glob', 'dummy_out_file')
                static_data_notifier_mock.assert_called_once_with(expected_paths, json.json_doc)

    def test_init_finds_files_in_input_directory(self):
        with patch('depict.output.json.FileSet') as fileset_mock:
            fake_include_glob = 'path/to/**/files*.py'
            Json(fake_include_glob, 'dummy_out_file')
            fileset_mock.assert_called_once_with(fake_include_glob)

    def test_runs_static_definition_notifier(self):
        with patch('depict.output.json.JsonDoc') as json_doc_class_mock:
            json = Json('dummy_input_block', 'dummy_out_file')
            json.static_data_notifier = Mock()
            json.run()
            json.static_data_notifier.run.assert_called_once_with()