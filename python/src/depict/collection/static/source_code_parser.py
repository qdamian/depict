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
from depict.collection.static.definitions_visitor import DefinitionsVisitor
from depict.collection.static.relations_visitor import RelationsVisitor
import sys

def astng_ignore_modname_wrapper(func, modname):
    '''A no-op decorator that must be passed to ASTNGManager to override its
       default behavior which is to print the module names to stdout'''
    try:
        return func(modname)
    except ASTNGBuildingException, exc:
        print exc
    except Exception, exc:
        import traceback
        traceback.print_exc()

class SourceCodeParser(object):
    '''Parse source files using LogiLab's Abstract Syntax Tree Next Generation
       and notify definitions and relations to observers'''

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

        # First collect all definitions (e.g. module X, function foo) before
        # trying to relate one definition with another (e.g. module X depends on
        # module Y)
        DefinitionsVisitor(self.observers).visit(project)
        RelationsVisitor(self.observers).visit(project)

    def register(self, observer):
        self.observers.append(observer)

    # pylint: disable=R0201
    def set_base_path(self, base_path):
        sys.path.insert(0, base_path)

# pylint: disable=C0103
GlobalSourceCodeParser = SourceCodeParser()
