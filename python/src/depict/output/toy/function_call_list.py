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

from depict.modeling.function_call_notifier import FunctionCallNotifier
from depict.modeling.def_collection_orchestrator import DefCollectionOrchestator
from depict.model.model import Model

class FunctionCallList(object):
    def __init__(self, out_filename, base_path):
        self.out_file = open(out_filename, 'w')
        orchestrator = DefCollectionOrchestator(base_path, Model())
        self.function_call_notifier = FunctionCallNotifier(self,
                            orchestrator.entity_id_generator,
                            orchestrator)
        self.stop = self.function_call_notifier.stop

    def start(self):
        self.function_call_notifier.start()

    def on_call(self, function_call):
        try:
            self.out_file.write(function_call.function.Class_.name + '.')
        except AttributeError:
            pass
        self.out_file.write(function_call.function.name + '\n')
