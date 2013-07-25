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

import ast

class PerformanceError(Exception):
    pass

class SourceCodeParser(ast.NodeVisitor):

    parsed_files = []

    def __init__(self):
        self.class_id = None
        self.class_col_offset = 0
        self.file_name = ''
        self.observers = []

    #pylint: disable=C0103
    def visit_ClassDef(self, node):
        id_ = self.file_name + ":" + str(node.lineno)
        self.class_id = id_
        self.class_col_offset = node.col_offset
        for observer in self.observers:
            try:
                observer.on_class(node.name, id_)
            except AttributeError:
                pass
        return super(SourceCodeParser, self).generic_visit(node)
  
    #pylint: disable=C0103
    def visit_FunctionDef(self, node):
        if node.col_offset <= self.class_col_offset:
            self.class_id = None
        id_ = self.file_name + ":" + str(node.lineno)
        for observer in self.observers:
            try:
                observer.on_function(node.name, id_, self.class_id)
            except AttributeError:
                pass
        return super(SourceCodeParser, self).generic_visit(node)
          
    def generic_visit(self, node):
        return super(SourceCodeParser, self).generic_visit(node)
    
    def parse(self, file_name, src_file):
        '''Raises any exception that ast.visit raises.
           E.g. SyntaxError, IndentationError'''
        if file_name in SourceCodeParser.parsed_files:
            raise PerformanceError(file_name)

        self.file_name = file_name
        content = str(src_file.read())
        root = ast.parse(content)
        SourceCodeParser.parsed_files.append(file_name)
        return super(SourceCodeParser, self).visit(root)

    def register(self, observer):
        self.observers.append(observer)

# pylint: disable=C0103
GlobalSourceCodeParser = SourceCodeParser()