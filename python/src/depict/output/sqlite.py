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

# pylint:disable = too-few-public-methods
class SQLite(object):
    def __init__(self, file_set, out_db, def_collection_orchestrator):
        self.file_set = file_set
        self.sqlite_db = SQLiteDB(out_db)
        self.static_data_notifier = StaticDataNotifier(file_set, self.sqlite_db,
                                                    def_collection_orchestrator)

    def run(self):
        self.static_data_notifier.run()
        self.sqlite_db.populate()