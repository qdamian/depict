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
import os
from depict.model import entity_id

class PerformanceError(Exception):
    pass

class SourceCodeParser(ast.NodeVisitor):
    parsed_files = []

    def __init__(self):
        self.class_id = None
        self.class_col_offset = 0
        self.file_name = ''
        self.observers = []

    def _safely_notify(self, function, args):
        for observer in self.observers:
            try:
                method = getattr(observer, function)
                # pylint: disable=W0142
                method(*args)
            except AttributeError:
                pass

    #pylint: disable=C0103
    def visit_ClassDef(self, node):
        id_ = self.file_name + ":" + str(node.lineno)
        self.class_id = id_
        self.class_col_offset = node.col_offset
        self._safely_notify('on_class', [id_, node.name])
        return super(SourceCodeParser, self).generic_visit(node)
  
    #pylint: disable=C0103
    def visit_FunctionDef(self, node):
        if node.col_offset <= self.class_col_offset:
            self.class_id = None
        id_ = self.file_name + ":" + str(node.lineno)
        self._safely_notify('on_function', [id_, node.name, self.class_id])
        return super(SourceCodeParser, self).generic_visit(node)

    def generic_visit(self, node):
        return super(SourceCodeParser, self).generic_visit(node)
    
    def parse(self, file_name, src_file):
        '''Raises any exception that ast.visit raises.
           E.g. SyntaxError, IndentationError'''
        if file_name in SourceCodeParser.parsed_files:
            raise PerformanceError(file_name)

        self.file_name = file_name
        self.notify_module()
        
        content = str(src_file.read())
        root = ast.parse(content)
        SourceCodeParser.parsed_files.append(file_name)
        return super(SourceCodeParser, self).visit(root)

    def notify_module(self):
        module_id = entity_id.create(self.file_name)
        module_name = '.'.join((os.path.splitext(module_id)[0]).split('/'))
        self._safely_notify('on_module', [module_id, module_name])

    def register(self, observer):
        self.observers.append(observer)

# pylint: disable=C0103
GlobalSourceCodeParser = SourceCodeParser()