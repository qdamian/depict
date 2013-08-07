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

from depict.model.module import Module
import unittest

class TestModule(unittest.TestCase):
    def test_creation(self):
        Module('fake_module_id', 'fake_module_name')

    def test_eq_comparison(self):
        module_1 = Module('fake_module_id1', 'dummy_module_name1')
        module_2 = Module('fake_module_id1', 'dummy_module_name2')
        self.assertEqual(module_1, module_2)