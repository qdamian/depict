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

class ModuleTable():
    def __init__(self, connection):
        self._connection = connection
    
    def create(self):
        self._connection.execute('''CREATE TABLE module(
                                        id VARCHAR PRIMARY KEY,
                                        name VARCHAR)''')
    
    def insert(self, function):
        pass
        self._connection.execute('''INSERT INTO module(id, name)
                                    VALUES (?, ?)''',
                                    (function.id_, function.name))