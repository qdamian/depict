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

from depict.model.function import Function

# pylint: disable=C0103, R0903
class Method(Function):
    def __init__(self, id_, name, Class_):
        super(Method, self).__init__(id_, name)
        self.Class_ = Class_
        
    def __repr__(self):
        return 'Method, name: ' + self.name + ', ID: ' + str(self.id_)