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

from depict.model.entity.class_ import Class_
from depict.model.entity.function import Function
from depict.persistence.sqlite.sqlite_db import SQLiteDB
from mock import Mock, patch, MagicMock
import unittest
from depict.model.entity.method import Method
from depict.model.entity.module import Module

class TestSQLiteDB(unittest.TestCase):

    def test_init_creates_db(self):
        with patch('depict.persistence.sqlite.sqlite_db.sqlite3') as sqlite3_mock:
            SQLiteDB('fake.db')
            sqlite3_mock.connect.assert_called_once_with('fake.db')

    def test_init_creates_module_table(self):
        with patch('depict.persistence.sqlite.sqlite_db.ModuleTable') as module_table_class_mock:
            module_table_mock = Mock()
            module_table_class_mock.return_value = module_table_mock
            SQLiteDB(':memory:')
            module_table_mock.create.assert_called_with()

    def test_init_creates_class_table(self):
        with patch('depict.persistence.sqlite.sqlite_db.ClassTable') as class_table_class_mock:
            class_table_mock = Mock()
            class_table_class_mock.return_value = class_table_mock
            SQLiteDB(':memory:')
            class_table_mock.create.assert_called_with()

    def test_init_creates_function_table(self):
        with patch('depict.persistence.sqlite.sqlite_db.FunctionTable') as function_table_class_mock:
            function_table_mock = Mock()
            function_table_class_mock.return_value = function_table_mock
            SQLiteDB(':memory:')
            function_table_mock.create.assert_called_with()

    def test_init_creates_method_table(self):
        with patch('depict.persistence.sqlite.sqlite_db.MethodTable') as method_table_class_mock:
            method_table_mock = Mock()
            method_table_class_mock.return_value = method_table_mock
            SQLiteDB(':memory:')
            method_table_mock.create.assert_called_with()

    def test_stores_each_module_def(self):
        with patch('depict.persistence.sqlite.sqlite_db.ModuleTable') as module_table_class_mock:
            module_table_mock = Mock()
            module_table_class_mock.return_value = module_table_mock
            sqlite_db = SQLiteDB(':memory:')
            dummy_module = Module('dummy_module_id', 'dummy_module_name')
            sqlite_db.on_module(dummy_module)
            module_table_mock.insert.assert_called_with(dummy_module)

    def test_stores_each_function_def(self):
        with patch('depict.persistence.sqlite.sqlite_db.FunctionTable') as function_table_class_mock:
            function_table_mock = Mock()
            function_table_class_mock.return_value = function_table_mock
            sqlite_db = SQLiteDB(':memory:')
            fake_function = Function('fake_function_id', 'fake_function_name')
            sqlite_db.on_function(fake_function)
            function_table_mock.insert.assert_called_with(fake_function)

    def test_stores_each_class_def(self):
        with patch('depict.persistence.sqlite.sqlite_db.ClassTable') as class_table_class_mock:
            class_table_mock = Mock()
            class_table_class_mock.return_value = class_table_mock
            sqlite_db = SQLiteDB(':memory:')
            fake_class = Class_('fake_class_id', 'fake_class_name')
            sqlite_db.on_class(fake_class)
            class_table_mock.insert.assert_called_with(fake_class)

    @patch('depict.persistence.sqlite.sqlite_db.FunctionTable')
    @patch('depict.persistence.sqlite.sqlite_db.MethodTable')
    def test_methods_reference_their_classes(self, function_table_class_mock, method_table_class_mock):
        function_table_mock = Mock()
        function_table_class_mock.return_value = function_table_mock
        method_table_mock = Mock()
        method_table_class_mock.return_value = method_table_mock
        sqlite_db = SQLiteDB(':memory:')
        fake_class = Class_('fake_class_id', 'fake_class_name')
        fake_method = Method('fake_method_id', 'fake_method_name', fake_class)
        sqlite_db.on_function(fake_method)
        function_table_mock.insert.assert_called_once_with(fake_method)
        method_table_mock.insert.assert_called_with(fake_method)

    def test_commits_sql_transactions(self):
        sqlite_db = SQLiteDB(':memory:')
        sqlite_db._connection = Mock()
        sqlite_db.populate()
        sqlite_db._connection.commit.assert_called_once_with()