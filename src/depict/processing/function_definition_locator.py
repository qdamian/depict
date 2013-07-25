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

from depict.model.function import Function
from depict.model.method import Method
from depict.model.class_repo import GlobalClassRepo
from depict.model.function_repo import GlobalFunctionRepo
from depict.collection.static.source_code_parser import GlobalSourceCodeParser

class FunctionDefinitionLocator():
    def __init__(self, source_code_parser = GlobalSourceCodeParser,
                 function_repo = GlobalFunctionRepo):
        self.source_code_parser = source_code_parser
        self.source_code_parser.register(self)
        self.function_repo = function_repo
    
    def process(self, file_name, src_code):
        self.source_code_parser.parse(file_name, src_code)
        
    def on_function(self, name, id_, class_id):
        if class_id:
            class_ = GlobalClassRepo.get(class_id)
            function = Method(name, id_, class_)
            class_.add_method(function)
        else:
            function = Function(name, id_) 
        self.function_repo.add(function)
