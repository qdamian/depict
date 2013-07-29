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

from depict.model.class_repo import GlobalClassRepo
from depict.model.function_repo import GlobalFunctionRepo
from depict.processing.class_definition_collector import \
    ClassDefinitionCollector
from depict.processing.definition_collection_orchestrator import \
    GlobalDefinitionCollectionOrchestrator
from depict.processing.function_definition_collector import \
    FunctionDefinitionCollector
from depict.processing.module_definition_collector import \
    ModuleDefinitionCollector
from depict.model.module_repo import GlobalModuleRepo

# pylint: disable=R0903
class StaticDataNotifier():
    def __init__(self, file_list, observer):
        self.observer = observer
        self.file_list = file_list
    
    def _safely_notify(self, function_name, value):
        try:
            notification_function = getattr(self.observer, function_name)
            notification_function(value)
        except AttributeError:
            pass

    def run(self):
        collection_orchestrator = GlobalDefinitionCollectionOrchestrator
        
        collection_orchestrator.include(ModuleDefinitionCollector)
        collection_orchestrator.include(ClassDefinitionCollector)
        collection_orchestrator.include(FunctionDefinitionCollector)
        
        for file_name in self.file_list:
            collection_orchestrator.process(file_name)

        for (func_name, repo) in [('on_module', GlobalModuleRepo),
                                  ('on_class', GlobalClassRepo),
                                  ('on_function', GlobalFunctionRepo)]:
            for value in repo.get_all():
                self._safely_notify(func_name, value)
