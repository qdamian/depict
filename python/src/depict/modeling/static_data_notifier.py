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

from depict.collection.static.source_code_parser import SourceCodeParser
from depict.modeling.class_def_collector import ClassDefCollector
from depict.modeling.def_collection_orchestrator import DefCollectionOrchestator
from depict.modeling.function_def_collector import FunctionDefCollector
from depict.modeling.module_def_collector import ModuleDefCollector

# pylint:disable = too-few-public-methods
class StaticDataNotifier(object):
    def __init__(self, file_set, observer, model):
        self.observer = observer
        self.file_set = file_set
        self.model = model
        self.def_collection_orchestrator = DefCollectionOrchestator(
                                                            file_set.directory)

    def _safely_notify(self, function_name, value=None):
        try:
            notification_function = getattr(self.observer, function_name)
            if value:
                notification_function(value)
            else:
                notification_function()
        except AttributeError:
            pass

    def run(self):
        self.def_collection_orchestrator.include(ModuleDefCollector)
        self.def_collection_orchestrator.include(ClassDefCollector)
        self.def_collection_orchestrator.include(FunctionDefCollector)

        source_code_parser = SourceCodeParser(self.file_set.directory)

        entity_id_gen = self.def_collection_orchestrator.entity_id_generator
        ModuleDefCollector(source_code_parser, entity_id_gen, self.model)

        file_list = [f for f in self.file_set]

        self.def_collection_orchestrator.process(file_list)

        for (func_name, repo) in [('on_module', self.model.modules),
                                  ('on_class', self.model.classes),
                                  ('on_function', self.model.functions)]:
            for value in repo.get_all():
                self._safely_notify(func_name, value)

        self._safely_notify('on_collection_completed')
