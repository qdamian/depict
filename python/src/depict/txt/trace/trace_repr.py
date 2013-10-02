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

from depict.model.model import Model
from depict.modeling.def_collection_orchestrator import DefCollectionOrchestator
from depict.modeling.function_call_notifier import FunctionCallNotifier
import sys

# pylint:disable = too-few-public-methods
class TraceRepr(object):

    def __init__(self, base_path):
        model = Model()
        orchestrator = DefCollectionOrchestator(base_path, model)
        self.function_call_notifier = FunctionCallNotifier(self,
                                            orchestrator.entity_id_generator,
                                            orchestrator)
        self.stop = self.function_call_notifier.stop

    # pylint:disable= no-self-use
    def on_call(self, function_call):
        line = '| '
        try:
            line += function_call.function.Class_.name + '.'
        except (AttributeError, KeyError):
            pass

        try:
            line += function_call.function.name + '\n'
        except KeyError:
            return
        sys.stdout.write(line)

    def start(self):
        self.function_call_notifier.start()
