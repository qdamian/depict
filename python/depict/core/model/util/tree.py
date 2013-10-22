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

class TreeNode(object):
    def __init__(self, parent):
        self.parent = parent
        self.children = []
        if parent:
            self.branch_depth = parent.branch_depth + 1
            parent.add_child(self)

    def add_child(self, node):
        self.children.append(node)


class TreeRootNode(TreeNode):
    def __init__(self):
        self.branch_depth = 0
        super(TreeRootNode, self).__init__(None)
