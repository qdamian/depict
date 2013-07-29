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

import sqlite3
from formic.formic import FileSet
from depict.processing.static_data_notifier import StaticDataNotifier
from depict.persistence.sqlite.class_table import ClassTable
from depict.persistence.sqlite.function_table import FunctionTable
from depict.persistence.sqlite.method_table import MethodTable
from depict.persistence.sqlite.module_table import ModuleTable

class SQLiteDB(object):

    # pylint: disable=W0201
    def __init__(self, input_glob, out_db):
        file_set = FileSet(input_glob)
        file_names = [name for name in file_set]
        self.static_data_notifier = StaticDataNotifier(file_names, self)
        self._connection = sqlite3.connect(out_db)
        self._create_tables()

    def _create_tables(self):
        self.module_table = ModuleTable(self._connection)
        self.class_table = ClassTable(self._connection)
        self.function_table = FunctionTable(self._connection)
        self.method_table = MethodTable(self._connection)
        for table in [self.module_table,
                      self.class_table,
                      self.function_table,
                      self.method_table]:
            table.create()

    def run(self):
        self.static_data_notifier.run()
        self._connection.commit()
    
    def on_function(self, function):
        self.function_table.insert(function)
        try:
            self.method_table.insert(function)
        except AttributeError:
            pass

    def on_class(self, class_):
        self.class_table.insert(class_)
    
    def on_module(self, module):
        self.module_table.insert(module)
