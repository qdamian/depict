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

from depict.model.entity.function import Function
from depict.persistence.sqlite.function_table import FunctionTable
from depict.test.template import real
from nose.tools import assert_true
import sqlite3

class TestFunctionTable():
    def test_table_creation(self):
        connection = sqlite3.connect(':memory:')
        function_table = FunctionTable(connection)
        function_table.create()
        connection.execute('SELECT id, name FROM function')

    def test_inserts_a_function(self):
        connection = sqlite3.connect(':memory:')
        function_table = FunctionTable(connection)
        function_table.create()
        fake_function = real('Function')
        function_table.insert(fake_function)
        cursor = connection.cursor()
        cursor.execute('''SELECT id, name FROM function
                          WHERE id = '%s' AND
                          name = '%s' ''' % (fake_function.id_,
                                             fake_function.name))
        assert_true(cursor.fetchone())