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

class SourceCodeParser(LocalsVisitor):

    def __init__(self):
        self.file_paths = []
        self.observers = []
        LocalsVisitor.__init__(self)

    def add_files(self, file_paths):
        if isinstance(file_paths, list):
            self.file_paths += file_paths
        else:
            self.file_paths = [file_paths]

    def _safely_notify(self, function, node):
        for observer in self.observers:
            try:
                method = getattr(observer, function)
                # pylint: disable=W0142
                method(node)
            except AttributeError:
                pass

    def visit_class(self, node):
        self._safely_notify('on_class', node)

    def visit_module(self, node):
        self._safely_notify('on_module', node)

    def visit_function(self, node):
        self._safely_notify('on_function', node)

    def visit_import(self, node):
        self._safely_notify('on_import', node)

    def visit_from(self, node):
        self._safely_notify('on_from', node)

    def parse(self):
        manager = ASTNGManager()
        project = manager.project_from_files(self.file_paths,
                                   func_wrapper = astng_ignore_modname_wrapper)
        self.visit(project)

    def register(self, observer):
        self.observers.append(observer)

# pylint: disable=C0103
GlobalSourceCodeParser = SourceCodeParser()