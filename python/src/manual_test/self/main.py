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

from depict.output.sqlite import SQLite
import sqlite3
from formic.formic import FileSet
from depict.modeling.def_collection_orchestrator import DefCollectionOrchestator

if __name__ == '__main__':
    db_name = 'self.sqlite.db'
    file_set = FileSet(directory='.', include='depict/**/*.py')
    sqlite = SQLite(file_set, db_name)
    sqlite.run()

    print 'Methods of the TestSQLiteDB class:'
    query = '''SELECT name FROM function WHERE id IN
          (SELECT  method.function_id FROM method, class
               WHERE method.class_id = class.id AND class.name = 'TestSQLiteDB')'''
    con = sqlite3.connect(db_name)
    for row in con.execute(query):
        print row

    print '\nClasses in the model:'
    query = '''SELECT class.name FROM class, module
               WHERE module.name LIKE '%model.%'
               AND NOT module.name LIKE '%test%'
               AND NOT module.name LIKE '%util%'
               AND class.module_id = module.id
               ORDER BY class.name'''
    con = sqlite3.connect(db_name)
    for row in con.execute(query):
        print row
