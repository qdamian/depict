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

from depict.processing.definition_collection_orchestrator import \
                                          GlobalDefinitionCollectionOrchestrator
from depict.model.class_repo import GlobalClassRepo
from depict.model.function_repo import GlobalFunctionRepo

class StaticDataNotifier():
    def __init__(self, file_list, observer):
        self.observer = observer
        self.file_list = file_list
    
    def run(self):
        collection_orchestrator = GlobalDefinitionCollectionOrchestrator()
        for f in self.file_list:
            collection_orchestrator.process(f)
        
        for class_ in GlobalClassRepo.get_all():
            self.observer.on_class(class_)

        for function in GlobalFunctionRepo.get_all():
            self.observer.on_function(function)