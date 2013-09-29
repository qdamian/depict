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

import os

# pylint:disable = too-few-public-methods
class EntityIdGenerator(object):
    '''
    Generate an identifier for a source code entity (node in the AST) based on
    the file name and line number in which the entity is found.

    Right now the id. is just a concatenation of the relative path to the file
    with respect to the project's base path plus the line number. Using this
    pattern for the id. helps in relating the static and dynamic data.
    Besides that, an id. generated in this way is stable across program
    executions (provided that the program didn't change).
    '''
    def __init__(self, base_path):
        self.base_path = base_path

    def create(self, file_name, line_number=None):
        generated_id = '%s' % os.path.relpath(file_name, self.base_path)
        if line_number:
            generated_id += ':%s' % line_number
        return generated_id