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

class SQLiteDB(object):

    def __init__(self, input_glob, out_db):
        file_set = FileSet(input_glob)
        file_names = [name for name in file_set]
        self.static_data_notifier = StaticDataNotifier(file_names, self)
        self._connection = sqlite3.connect(out_db)
        self._create_tables()

    def _create_tables(self):            
        self._connection.execute('''CREATE TABLE class(
                                        id VARCHAR PRIMARY KEY,
                                        name VARCHAR)''')
        self._connection.execute('''CREATE TABLE function(
                                        id VARCHAR PRIMARY KEY,
                                        name VARCHAR)''')
        self._connection.execute('''CREATE TABLE method(
                    class_id VARCHAR,
                    function_id VARCHAR,
                    PRIMARY KEY(class_id, function_id),
                    FOREIGN KEY(class_id) REFERENCES class(id),
                    FOREIGN KEY(function_id) REFERENCES function(id))''')

    def run(self):
        self.static_data_notifier.run()
        self._connection.commit()
    
    def on_function(self, function):
        self._connection.execute('''INSERT INTO function(id, name)
                                    VALUES (?, ?)''',
                                    (function.id_, function.name))    

        cursor = self._connection.cursor()
        cursor.execute('''SELECT * FROM function''')

        try:
            self._connection.execute('''INSERT INTO method(class_id,
                                        function_id) VALUES (?, ?)''',
                                        (function.Class_.id_,
                                         function.id_))
        except AttributeError:
            pass

    def on_class(self, class_):
        self._connection.execute('''INSERT INTO class(id, name)
                                    VALUES (?, ?)''',
                                    (class_.id_, class_.name))    