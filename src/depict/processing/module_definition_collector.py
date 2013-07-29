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

from depict.collection.static.source_code_parser import GlobalSourceCodeParser
from depict.model.module import Module
from depict.model.module_repo import GlobalModuleRepo

# pylint: disable=R0903
class ModuleDefinitionCollector():
    def __init__(self, source_code_parser = GlobalSourceCodeParser,
                 module_repo = GlobalModuleRepo):
        source_code_parser.register(self)
        self.module_repo = module_repo
        
    def on_module(self, id_, name):
        self.module_repo.add(Module(id_, name))