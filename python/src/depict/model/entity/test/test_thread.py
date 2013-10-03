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

from depict.model.entity.thread import Thread
from nose.tools import assert_equal, assert_true
from depict.model.util.tree import RootNode

class TestFunction():
    def test_creation(self):
        Thread('fake_thread_id')

    def test_equal_comparison(self):
        thread1 = Thread('fake_thread_id')
        thread2 = Thread('fake_thread_id')
        assert_equal(thread1, thread2)

    def test_is_a_tree_root_node(self):
        assert_true(isinstance(Thread(''), RootNode))
