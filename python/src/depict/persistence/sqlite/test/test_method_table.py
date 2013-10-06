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

from depict.model.entity.class_ import Class_
from depict.model.entity.method import Method
from depict.persistence.sqlite.method_table import MethodTable
from depict.test.template import real
from nose.tools import assert_true
import sqlite3

class TestMethodTable():
    def test_table_creation(self):
        connection = sqlite3.connect(':memory:')
        method_table = MethodTable(connection)
        method_table.create()
        connection.execute('SELECT class_id, function_id FROM method')

    def test_insert_method_relates_class_and_function(self):
        connection = sqlite3.connect(':memory:')
        method_table = MethodTable(connection)
        method_table.create()
        fake_class = real('Class_')
        fake_method = real('Method')
        method_table.insert(fake_method)
        cursor = connection.cursor()
        cursor.execute('''SELECT function_id, class_id FROM method
                          WHERE function_id = '%s' AND
                          class_id = '%s' ''' % (fake_method.id_,
                                                 fake_class.id_))
        assert_true(cursor.fetchone())