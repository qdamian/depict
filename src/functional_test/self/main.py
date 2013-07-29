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

#!/usr/bin/env python

from depict.presentation.toy.definition_list import DefinitionList
from depict.persistence.sqlite.sqlite_db import SQLiteDB
import sqlite3

if __name__ == '__main__':
    definition_list = DefinitionList('src/*.py', 'self.definition_list.out')
    db_name = 'self.sqlite.db'
    sqlite_db = SQLiteDB('*.py', db_name)
    definition_list.run()
    sqlite_db.run()

    print 'Methods of the TestSQLiteDB class:'
    query = '''SELECT name FROM function WHERE id IN
          (SELECT  method.function_id FROM method, class
               WHERE method.class_id = class.id AND class.name = 'TestSQLiteDB')'''
    con = sqlite3.connect(db_name)
    for row in con.execute(query):
        print row
