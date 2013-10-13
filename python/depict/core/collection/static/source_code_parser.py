# Copyright 2013 Damian Quiroga
#
# This file is part of depict.
#
# depict is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# depict is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with depict.  If not, see <http://www.gnu.org/licenses/>.

from depict.core.collection.static.defs_visitor import DefsVisitor
from depict.core.collection.static.relations_visitor import RelationsVisitor
from depict.core.model.util.entity_id_generator import EntityIdGenerator
from astroid.exceptions import AstroidBuildingException
from astroid.manager import AstroidManager
import sys

class SourceCodeParser(object):
    '''
    Parse source files using Astroid and notify definitions and relations to
    observers.

    The source files to parse are specified by the user of this class by passing
    a "base path" on construction (root of the program to be analyzed) and
    relative paths to the source files later.
    '''

    def __init__(self, base_path):
        self.file_paths = set()
        self.observers = set()
        self.entity_id_gen = EntityIdGenerator(base_path)
        # For ASTNManager:
        sys.path.insert(0, base_path)

    def add_files(self, paths):
        '''Try to add the given path(s). Return True if at least one path was
           added, False otherwise'''
        if not isinstance(paths, list):
            paths = [paths]

        len_before = len(self.file_paths)
        self.file_paths.update(paths)
        return len(self.file_paths) != len_before

    def register(self, observer):
        self.observers.update([observer])

    def parse(self):
        manager = AstroidManager()
        project = manager.project_from_files(list(self.file_paths),
                                func_wrapper = astroid_ignore_modname_wrapper)

        # First collect all definitions (e.g. module X, function foo) before
        # trying to relate one definition with another (e.g. module X depends on
        # module Y)
        DefsVisitor(self.observers).visit(project)
        RelationsVisitor(self.observers).visit(project)

def astroid_ignore_modname_wrapper(func, modname):
    '''A no-op decorator that must be passed to AstroidManager to override its
       default behavior which is to print the module names to stdout'''
    try:
        return func(modname)
    except AstroidBuildingException, exc:
        print exc
    except Exception, exc:
        import traceback
        traceback.print_exc()