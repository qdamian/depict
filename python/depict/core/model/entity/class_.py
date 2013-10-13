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

from depict.core.model.util.tree import TreeNode

# pylint:disable = invalid-name
class Class_(TreeNode):
    '''Represent a class'''

    def __init__(self, id_, name, module):
        self.id_ = id_
        self.name = name
        self.module = module
        super(Class_, self).__init__(module)

    def add_method(self, method):
        pass

    def __eq__(self, other):
        return self.id_ == other.id_

    def __repr__(self):
        return str(self.__dict__)
