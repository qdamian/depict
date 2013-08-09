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

from logilab.astng.manager import ASTNGManager
from logilab.astng.exceptions import ASTNGBuildingException
from logilab.astng.utils import LocalsVisitor

def astng_ignore_modname_wrapper(func, modname):
    try:
        return func(modname)
    except ASTNGBuildingException, exc:
        print exc
    except Exception, exc:
        import traceback
        traceback.print_exc()

def _safely_notify(observers, function, node):
    for obs in observers:
        try:
            method = getattr(obs, function)
            # pylint: disable=W0142
            method(node)
        except AttributeError:
            pass

class DefinitionsVisitor(LocalsVisitor):

    def __init__(self, observers):
        LocalsVisitor.__init__(self)
        self.observers = observers

    def visit_class(self, node):
        _safely_notify(self.observers, 'on_class', node)

    def visit_module(self, node):
        _safely_notify(self.observers, 'on_module', node)

    def visit_function(self, node):
        _safely_notify(self.observers, 'on_function', node)

class RelationsVisitor(LocalsVisitor):
    def visit_module(self, node):
        _safely_notify(self.observers, 'on_module', node)

    def __init__(self, observers):
        LocalsVisitor.__init__(self)
        self.observers = observers

    def visit_import(self, node):
        _safely_notify(self.observers, 'on_import', node)

    def visit_from(self, node):
        _safely_notify(self.observers, 'on_from', node)

class SourceCodeParser(object):

    def __init__(self):
        self.file_paths = []
        self.observers = []

    def add_files(self, file_paths):
        if isinstance(file_paths, list):
            self.file_paths += file_paths
        else:
            self.file_paths = [file_paths]

    def parse(self):
        manager = ASTNGManager()
        project = manager.project_from_files(self.file_paths,
                                   func_wrapper = astng_ignore_modname_wrapper)

        # First collect all "definitions" (modules, classes, functions) before
        # trying to relate one definition with another

        definitions_visitor = DefinitionsVisitor(self.observers)
        definitions_visitor.visit(project)

        relations_visitor = RelationsVisitor(self.observers)
        relations_visitor.visit(project)

    def register(self, observer):
        self.observers.append(observer)

# pylint: disable=C0103
GlobalSourceCodeParser = SourceCodeParser()