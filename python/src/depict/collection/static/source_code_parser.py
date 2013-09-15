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

from depict.collection.static.definitions_visitor import DefinitionsVisitor
from depict.collection.static.relations_visitor import RelationsVisitor
from depict.model.util.entity_id_generator import EntityIdGenerator
from logilab.astng.exceptions import ASTNGBuildingException
from logilab.astng.manager import ASTNGManager
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

    def __init__(self, base_path):
        self.file_paths = set()
        self.observers = []
        self.entity_id_gen = EntityIdGenerator(base_path)
        # For ASTNManager:
        sys.path.insert(0, base_path)

    def add_files(self, paths):
        if not isinstance(paths, list):
            paths = [paths]

        len_before = len(self.file_paths)
        self.file_paths.update(paths)
        return len(self.file_paths) != len_before

    def parse(self):
        manager = ASTNGManager()
        project = manager.project_from_files(list(self.file_paths),
                                   func_wrapper = astng_ignore_modname_wrapper)

        # First collect all definitions (e.g. module X, function foo) before
        # trying to relate one definition with another (e.g. module X depends on
        # module Y)
        DefinitionsVisitor(self.observers).visit(project)
        RelationsVisitor(self.observers).visit(project)

    def register(self, observer):
        self.observers.append(observer)
