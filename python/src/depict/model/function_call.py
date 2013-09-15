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

from depict.model.util.function_repo import global_function_repo

# pylint:disable = too-few-public-methods
class FunctionCall(object):
    def __init__(self, function_id):
        self.function_id = function_id

    @property
    def function(self):
        return global_function_repo.get_by_id(self.function_id)

    def __eq__(self, other):
        return self.function_id == other.function_id

    def __repr__(self):
        return 'ID: ' + self.function_id