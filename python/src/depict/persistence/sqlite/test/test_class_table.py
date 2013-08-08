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
from depict.persistence.sqlite.class_table import ClassTable
import sqlite3
import unittest
from depict.model.module import Module

class TestClassTable(unittest.TestCase):
    def test_table_creation(self):
        connection = sqlite3.connect(':memory:')
        class_table = ClassTable(connection)
        class_table.create()
        connection.execute('SELECT id, name FROM class')

    def test_inserts_a_class(self):
        connection = sqlite3.connect(':memory:')
        class_table = ClassTable(connection)
        class_table.create()
        dummy_module = Module('fake_module_id', 'fake_module_name')
        fake_class = Class_('fake_class_id', 'fake_class_name', dummy_module)
        class_table.insert(fake_class)
        cursor = connection.cursor()
        cursor.execute('''SELECT id, name FROM class
                          WHERE id = 'fake_class_id' AND
                          name = 'fake_class_name' ''')
        self.assertTrue(cursor.fetchone())

    def test_insert_class_relates_it_to_module(self):
        connection = sqlite3.connect(':memory:')
        class_table = ClassTable(connection)
        class_table.create()
        fake_module = Module('fake_module_id', 'fake_module_name')
        fake_class = Class_('fake_class_id', 'fake_class_name', fake_module)
        class_table.insert(fake_class)
        cursor = connection.cursor()
        cursor.execute('''SELECT module_id FROM class
                          WHERE id = 'fake_class_id' ''')
        actual_module_id = cursor.fetchone()
        self.assertEqual(actual_module_id[0], 'fake_module_id')
