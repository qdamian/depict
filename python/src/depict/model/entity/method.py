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

from depict.model.entity.function import Function

# pylint:disable = invalid-name, too-few-public-methods
class Method(Function):
    '''Represent a class method'''

    def __init__(self, id_, name, Class_):
        super(Method, self).__init__(id_, name)
        self.Class_ = Class_

    def __repr__(self):
        return str(self.__dict__)