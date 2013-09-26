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

from depict.model.entity.function import Function
from depict.persistence.sqlite.function_table import FunctionTable
import sqlite3
import unittest

class TestFunctionTable(unittest.TestCase):
    def test_table_creation(self):
        connection = sqlite3.connect(':memory:')
        function_table = FunctionTable(connection)
        function_table.create()
        connection.execute('SELECT id, name FROM function')

    def test_inserts_a_function(self):
        connection = sqlite3.connect(':memory:')
        function_table = FunctionTable(connection)
        function_table.create()
        fake_class = Function('fake_function_id', 'fake_function_name')
        function_table.insert(fake_class)
        cursor = connection.cursor()
        cursor.execute('''SELECT id, name FROM function
                          WHERE id = 'fake_function_id' AND
                          name = 'fake_function_name' ''')
        self.assertTrue(cursor.fetchone())