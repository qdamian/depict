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

from logilab.astng.utils import LocalsVisitor
from depict.collection.static.notifier import safely_notify

class DefinitionsVisitor(LocalsVisitor):

    def __init__(self, observers):
        LocalsVisitor.__init__(self)
        self.observers = observers

    def visit_class(self, node):
        safely_notify(self.observers, 'on_class', node)

    def visit_module(self, node):
        safely_notify(self.observers, 'on_module', node)

    def visit_function(self, node):
        safely_notify(self.observers, 'on_function', node)