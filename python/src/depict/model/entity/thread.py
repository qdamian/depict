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

from depict.model.util.tree import RootNode

# pylint:disable = too-few-public-methods
class Thread(RootNode):
    '''Represent a thread such as the MainThread'''

    def __init__(self, id_):
        self.id_ = id_
        super(Thread, self).__init__()

    def __eq__(self, other):
        return other.id_ == self.id_

    def __repr__(self):
        return str(self.__dict__)