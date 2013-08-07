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

from depict.persistence.sqlite.sqlite_db import SQLiteDB
from depict.modeling.static_data_notifier import StaticDataNotifier
from formic.formic import FileSet

# pylint: disable=R0903
class SQLite(object):

    def __init__(self, input_glob, out_db):
        self.sqlite_db = SQLiteDB(out_db)
        file_set = FileSet(input_glob)
        file_names = [name for name in file_set]
        self.static_data_notifier = StaticDataNotifier(file_names,
                                                       self.sqlite_db)

    def run(self):
        self.static_data_notifier.run()
        self.sqlite_db.populate()