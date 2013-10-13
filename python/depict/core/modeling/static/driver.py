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

from depict.core.collection.static.source_code_parser import SourceCodeParser
from depict.core.modeling.static.class_ import Class_
from depict.core.modeling.orchestrator import Orchestrator
from depict.core.modeling.static.function import Function
from depict.core.modeling.static.module import Module

class Driver(object):
    def __init__(self, file_set, observer, model):
        self.observer = observer
        self.file_set = file_set
        self.model = model
        self.orchestrator = Orchestrator(file_set.directory, self.model)

    def _best_effort_notify(self, function_name, value=None):
        try:
            notification_function = getattr(self.observer, function_name)
            if value:
                notification_function(value)
            else:
                notification_function()
        except AttributeError:
            pass

    def run(self):
        self.orchestrator.include(Module)
        self.orchestrator.include(Class_)
        self.orchestrator.include(Function)

        file_list = [f for f in self.file_set]

        self.orchestrator.process(file_list)

        for (func_name, repo) in [('on_module', self.model.modules),
                                  ('on_class', self.model.classes),
                                  ('on_function', self.model.functions)]:
            for value in repo.get_all():
                self._best_effort_notify(func_name, value)

        return self.model
