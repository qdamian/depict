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

from depict.model.entity.module import Module
import unittest
from nose.tools import *

class TestModule(unittest.TestCase):
    def test_creation(self):
        Module('fake_module_id', 'fake_module_name')

    def test_eq_comparison(self):
        module1 = Module('fake_module_id1', 'dummy_module_name1')
        module2 = Module('fake_module_id1', 'dummy_module_name2')
        self.assertEqual(module1, module2)

    def test_learns_one_dependency(self):
        module1 = Module('fake_module_id1', 'dummy_module_name1')
        module2 = Module('fake_module_id2', 'dummy_module_name2')
        module2.depends_on(module1)
        assert_equal(module2.dependencies, [module1])

    def test_learns_two_dependencies(self):
        module1 = Module('fake_module_id1', 'dummy_module_name1')
        module2 = Module('fake_module_id2', 'dummy_module_name2')
        module3 = Module('fake_module_id3', 'dummy_module_name3')
        module3.depends_on([module1, module2])
        assert_equal(module3.dependencies, [module1, module2])
