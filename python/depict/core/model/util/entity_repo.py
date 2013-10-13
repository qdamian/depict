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


class EntityRepo(object):
    def __init__(self):
        self.elements_by_id = {}
        self.elements_by_name = {}

    def add(self, element):
        assert element.id_, 'The element is expected to have an id_ attribute'

        self.elements_by_id[element.id_] = element
        try:
            self.elements_by_name[element.name] = element
        except AttributeError:
            pass

    def get_by_id(self, id_):
        return self.elements_by_id[id_]

    def get_by_name(self, name):
        return self.elements_by_name[name]

    def get_all(self):
        return self.elements_by_id.values()
