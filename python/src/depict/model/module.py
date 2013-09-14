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

# pylint:disable = invalid-name, too-few-public-methods

class Module(object):
    def __init__(self, id_, name):
        self.id_ = id_
        self.name = name
        self.dependencies = []

    def __eq__(self, other):
        return self.id_ == other.id_

    def depends_on(self, modules):
        try:
            self.dependencies.extend(modules)
        except TypeError:
            self.dependencies.append(modules)
