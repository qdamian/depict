#region GPLv3 notice
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
#endregion

from astroid.utils import LocalsVisitor
from depict.core.collection.static.notifier import best_effort_notify

class RelationsVisitor(LocalsVisitor):
    '''
    Visit the project notifying the observers about (some types of) relations
    found between entities. Nodes that define an entity are not notified.
    '''
    def __init__(self, observers):
        LocalsVisitor.__init__(self)
        self.observers = observers
        self.currently_visited_module = None

    def visit_module(self, node):
        self.currently_visited_module = node

    def visit_import(self, node):
        best_effort_notify(self.observers, 'on_import',
                           self.currently_visited_module, node)

    def visit_from(self, node):
        best_effort_notify(self.observers, 'on_from',
                           self.currently_visited_module, node)