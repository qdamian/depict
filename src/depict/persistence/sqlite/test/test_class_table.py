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
        fake_class = Class_('fake_class_id', 'fake_class_name')
        class_table.insert(fake_class)
        cursor = connection.cursor()
        cursor.execute('''SELECT id, name FROM class
                          WHERE id = 'fake_class_id' AND
                          name = 'fake_class_name' ''')
        self.assertTrue(cursor.fetchone())