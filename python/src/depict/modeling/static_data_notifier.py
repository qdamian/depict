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

from depict.modeling.class_definition_collector import ClassDefinitionCollector
from depict.modeling.module_definition_collector import \
                                                      ModuleDefinitionCollector
from depict.modeling.function_definition_collector import \
                                                    FunctionDefinitionCollector
from depict.collection.static.source_code_parser import SourceCodeParser
from depict.model.util.module_repo import global_module_repo
from depict.model.util.class_repo import global_class_repo
from depict.model.util.function_repo import global_function_repo

# pylint:disable = too-few-public-methods
class StaticDataNotifier(object):
    def __init__(self, file_set, observer, def_collection_orchestrator):
        self.observer = observer
        self.file_set = file_set
        self.def_collection_orchestrator = def_collection_orchestrator

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
        self.def_collection_orchestrator.include(ModuleDefinitionCollector)
        self.def_collection_orchestrator.include(ClassDefinitionCollector)
        self.def_collection_orchestrator.include(FunctionDefinitionCollector)

        source_code_parser = SourceCodeParser(self.file_set.directory)

        entity_id_gen = self.def_collection_orchestrator.entity_id_generator
        ModuleDefinitionCollector(source_code_parser, entity_id_gen)

        file_list = [f for f in self.file_set]

        self.def_collection_orchestrator.process(file_list)

        for (func_name, repo) in [('on_module', global_module_repo),
                                  ('on_class', global_class_repo),
                                  ('on_function', global_function_repo)]:
            for value in repo.get_all():
                self._safely_notify(func_name, value)

        self._safely_notify('on_collection_completed')
