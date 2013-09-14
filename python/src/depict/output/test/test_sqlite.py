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

from depict.output.sqlite import SQLite
from mock import patch, MagicMock, Mock
import unittest
from formic.formic import FileSet

class TestSQLite(unittest.TestCase):

    def test_init_creates_static_data_notifier(self):
        with patch('depict.output.sqlite.StaticDataNotifier') as static_data_notifier_mock:
            expected_paths = ['fake/file/a.py', 'file/file/b.py']
            fileset_mock = Mock()
            def_collection_orchestrator_mock = Mock()

            sqlite = SQLite(fileset_mock, ':memory:', def_collection_orchestrator_mock)

            static_data_notifier_mock.assert_called_once_with(fileset_mock, sqlite.sqlite_db,
                                                              def_collection_orchestrator_mock)

    def test_init_creates_sqlite_db(self):
        with patch('depict.output.sqlite.SQLiteDB') as sqlite_db_class_mock:
            SQLite('dummy_input_glob', 'fake_out_db', Mock())
            sqlite_db_class_mock.assert_called_once_with('fake_out_db')

    def test_runs_static_definition_notifier(self):
        sqlite = SQLite('dummy_file_set', ':memory:', Mock())
        sqlite.static_data_notifier = Mock()
        module_repo = Mock()
        class_repo = Mock()
        function_repo = Mock()
        sqlite.run()
        sqlite.static_data_notifier.run.assert_called_once_with()

    def test_run_populates_db(self):
        with patch('depict.output.sqlite.SQLiteDB') as sqlite_db_class_mock:
            sqlite_db_mock = Mock()
            sqlite_db_class_mock.return_value = sqlite_db_mock
            file_set = MagicMock()
            file_set.directory = '.'
            sqlite = SQLite(file_set, 'fake_out_db', Mock())
            sqlite.run()
            sqlite_db_mock.populate.assert_called_once_with()
