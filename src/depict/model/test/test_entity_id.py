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

import unittest
from depict.model import entity_id
from mock import patch

class TestEntityId(unittest.TestCase):
    @patch('depict.model.entity_id.os.path.relpath')
    def test_removes_working_directory_from_file_name(self, relpath_mock):   
        relpath_mock.return_value = 'some/file.py'
        actual_id = entity_id.create('full/path/to/some/file.py', '12')
        expected_id = 'some/file.py:12'
        self.assertEqual(actual_id, expected_id)

    def test_line_number_is_optional(self):
        expected_id = 'dummy_file_name'
        actual_id = entity_id.create('dummy_file_name')
        self.assertEqual(actual_id, expected_id)
        
    def test_works_with_int_line_number(self):
        expected_id = 'dummy_file_name:3'
        actual_id = entity_id.create('dummy_file_name', 3)
        self.assertEqual(actual_id, expected_id)
