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
from depict.persistency.sqlite_db import SQLiteDB
from mock import Mock, patch, MagicMock
import unittest
from depict.model.method import Method

class TestSQLiteDB(unittest.TestCase):

    def test_init_creates_db(self):
        with patch('depict.persistency.sqlite_db.sqlite3') as sqlite3_mock:
            SQLiteDB('dummy_file_glob', 'fake.db')
            sqlite3_mock.connect.assert_called_once_with('fake.db')

    def test_init_creates_class_table(self):
        sqlite_db = SQLiteDB('dummy_file_glob', ':memory:')
        sqlite_db._connection.execute('SELECT id, name FROM class')

    def test_init_creates_function_table(self):
        sqlite_db = SQLiteDB('dummy_file_glob', ':memory:')
        sqlite_db._connection.execute('SELECT id, name FROM function')

    def test_init_creates_method_table(self):
        sqlite_db = SQLiteDB('dummy_file_glob', ':memory:')
        sqlite_db._connection.execute('SELECT function_id, class_id FROM method')

    def test_init_finds_files_in_input_directory(self):
        with patch('depict.persistency.sqlite_db.FileSet') as fileset_mock:
            fake_include_glob = 'path/to/**/files*.py'
            SQLiteDB(fake_include_glob, ':memory:')
            fileset_mock.assert_called_once_with(fake_include_glob)
 
    def test_init_creates_static_data_notifier(self):
        with patch('depict.persistency.sqlite_db.StaticDataNotifier') as static_data_notifier_mock:
            with patch('depict.persistency.sqlite_db.FileSet') as fileset_class_mock:
                expected_paths = ['fake/file/a.py', 'file/file/b.py']
                fileset_mock = MagicMock()
                fileset_mock.__iter__.return_value = expected_paths
                fileset_class_mock.return_value = fileset_mock
                sqlite_db = SQLiteDB('dummy_input_glob', ':memory:')
                static_data_notifier_mock.assert_called_once_with(expected_paths, sqlite_db)
  
    def test_runs_static_definition_notifier(self):
        sqlite_db = SQLiteDB('dummy_input_glob', ':memory:')
        sqlite_db.static_data_notifier = Mock()
        sqlite_db.run()
        sqlite_db.static_data_notifier.run.assert_called_once_with()
 
    def test_stores_each_function_definition(self):
        sqlite_db = SQLiteDB('dummy_input_glob', ':memory:')
        fake_function = Function('fake_function_name', 'fake_function_id')
        sqlite_db.on_function(fake_function)
        cursor = sqlite_db._connection.cursor()
        cursor.execute('''SELECT id, name FROM function
                          WHERE id = 'fake_function_id' AND
                          name = 'fake_function_name' ''')
        self.assertTrue(cursor.fetchone())
 
    def test_stores_each_class_definition(self):
        sqlite_db = SQLiteDB('dummy_input_glob', ':memory:')
        fake_class = Class_('fake_class_name', 'fake_class_id')
        sqlite_db.on_class(fake_class)
        cursor = sqlite_db._connection.cursor()
        cursor.execute('''SELECT id, name FROM class
                          WHERE id = 'fake_class_id' AND
                          name = 'fake_class_name' ''')
        self.assertTrue(cursor.fetchone())

    def test_methods_refer_to_their_classes(self):
        sqlite_db = SQLiteDB('dummy_input_glob', ':memory:')
        fake_class = Class_('fake_class_name', 'fake_class_id')
        fake_method = Method('fake_method_name', 'fake_method_id', fake_class)
        sqlite_db.on_function(fake_method)
        cursor = sqlite_db._connection.cursor()
        cursor.execute('''SELECT id, name FROM function
                          WHERE id = 'fake_method_id' AND
                          name = 'fake_method_name' ''')
        self.assertTrue(cursor.fetchone())
        cursor.execute('''SELECT function_id, class_id FROM method
                          WHERE function_id = 'fake_method_id' AND
                          class_id = 'fake_class_id' ''')
        self.assertTrue(cursor.fetchone())