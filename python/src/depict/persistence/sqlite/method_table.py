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

class MethodTable(object):
    def __init__(self, connection):
        self._connection = connection

    def create(self):
        self._connection.execute('''CREATE TABLE method(
                    class_id VARCHAR,
                    function_id VARCHAR,
                    PRIMARY KEY(class_id, function_id),
                    FOREIGN KEY(class_id) REFERENCES class(id),
                    FOREIGN KEY(function_id) REFERENCES function(id))''')

    def insert(self, function):
        self._connection.execute('''INSERT INTO method(class_id,
                                    function_id) VALUES (?, ?)''',
                                    (function.Class_.id_, function.id_))