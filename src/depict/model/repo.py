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

class Repo(object):
    def __init__(self):
        self.elements = {}
    
    def add(self, element):
        '''
        The element is expected to have an id_ attribute
        '''
        self.elements[element.id_] = element
    
    def get(self, id_):
        try:
            return self.elements[id_]
        except KeyError:
            return None