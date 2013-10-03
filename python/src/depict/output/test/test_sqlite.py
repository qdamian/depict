# Copyright 2013 Damian Quiroga
#
# This file is part of depict.
#
# depict is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# depict is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with depict.  If not, see <http://www.gnu.org/licenses/>.

from depict.output.sqlite import SQLite
from mock import patch, MagicMock, Mock, ANY
import unittest
from formic.formic import FileSet
from depict.model.model import Model

class TestSQLite(unittest.TestCase):

    def test_init_creates_static_data_notifier(self):
        with patch('depict.output.sqlite.StaticDataNotifier') as static_data_notifier_mock:
            expected_paths = ['fake/file/a.py', 'file/file/b.py']
            fileset_mock = Mock()

            sqlite = SQLite(fileset_mock, ':memory:')

            static_data_notifier_mock.assert_called_once_with(fileset_mock, sqlite.sqlite_db, ANY)

    def test_init_creates_sqlite_db(self):
        with patch('depict.output.sqlite.SQLiteDB') as sqlite_db_class_mock:
            file_set = Mock()
            file_set.directory = '.'
            SQLite(file_set, 'fake_out_db')
            sqlite_db_class_mock.assert_called_once_with('fake_out_db')

    def test_runs_static_def_notifier(self):
        file_set = FileSet(directory='.', include='*')
        sqlite = SQLite(file_set, ':memory:')
        sqlite.static_data_notifier = Mock()
        module_repo = Mock()
        class_repo = Mock()
        function_repo = Mock()
        sqlite.run()
        sqlite.static_data_notifier.run.assert_called_once_with()

    @patch('depict.output.sqlite.StaticDataNotifier', autospec=True)
    @patch('depict.output.sqlite.SQLiteDB', autospec=True)
    def test_run_populates_db(self, sqlite_db_class_mock, static_data_notifier_mock):
            sqlite_db_mock = Mock()
            sqlite_db_class_mock.return_value = sqlite_db_mock
            file_set = MagicMock()
            file_set.directory = '.'
            sqlite = SQLite(file_set, 'fake_out_db')
            sqlite.run()
            sqlite_db_mock.populate.assert_called_once_with()
