#region GPLv3 notice
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
#endregion

from depict.core.modeling.static.class_ import Class_
from depict.core.modeling.orchestrator import Orchestrator
from depict.core.modeling.static.function import Function
from depict.core.modeling.static.module import Module

class Driver(object):
    def __init__(self, file_set, model):
        self.file_set = file_set
        self.model = model

    def run(self):
        orchestrator = Orchestrator(self.file_set.directory, self.model)
        orchestrator.include(Module)
        orchestrator.include(Class_)
        orchestrator.include(Function)

        file_list = [f for f in self.file_set]

        orchestrator.process(file_list)

        return self.model
