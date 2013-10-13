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

from depict.core.collection.dynamic.frame_digest import FrameDigest
from mock import Mock, MagicMock, patch
from nose_parameterized import parameterized
from nose.tools import *
import inspect

class TestFrameDigest():

    @parameterized.expand([('module1',), ('module2',)])
    def test_it_learns_the_module_name_from_the_frame(self, expected_module_name):
        # Arrange
        frame_mock = Mock()
        frame_mock.f_globals = MagicMock()
        frame_mock.f_globals.__getitem__.return_value = expected_module_name
        frame_digest = FrameDigest(frame_mock)

        # Act
        actual_module_name = frame_digest.module_name

        # Assert
        assert_equal(actual_module_name, expected_module_name)

    @patch('os.path.abspath', autospec=True)
    def test_file_name_returns_full_path_to_file(self, abspath_mock):
        # Arrange
        abspath_mock.return_value = 'absolute/path/to/file'
        frame_mock = Mock()
        frame_mock.f_code.co_filename = 'path/to/file'
        frame_digest = FrameDigest(frame_mock)

        # Act
        actual_filename = frame_digest.file_name

        # Assert
        abspath_mock.assert_called_once_with('path/to/file')
        assert_equal(actual_filename, 'absolute/path/to/file')

    @parameterized.expand([('func1',), ('func2',)])
    def test_it_learns_the_function_name_from_the_frame(self, expected_function_name):
        # Arrange
        frame_mock = Mock()
        frame_mock.f_code.co_name = expected_function_name
        frame_digest = FrameDigest(frame_mock)

        # Act
        actual_function_name = frame_digest.function_name

        # Assert
        assert_equal(actual_function_name, expected_function_name)

    @parameterized.expand([(1,), (10,)])
    def test_line_number_returns_source_code_line_number(self, expected_lineno):
        # Arrange
        frame_mock = Mock()
        frame_mock.f_lineno = expected_lineno
        frame_digest = FrameDigest(frame_mock)

        # Act
        actual_lineno = frame_digest.line_number

        # Assert
        assert_equal(actual_lineno, expected_lineno)

    def test_works_on_a_real_frame_object(self):
        # Arrange
        frame = inspect.currentframe()
        frame_digest = FrameDigest(frame)

        # Act
        actual_module_name = frame_digest.module_name
        actual_function_name = frame_digest.function_name
        actual_file_name = frame_digest.file_name
        actual_lineno = frame_digest.line_number

        # Assert
        assert_in('test_frame_digest', actual_module_name)
        assert_equal(actual_function_name, 'test_works_on_a_real_frame_object')
        assert_in('test_frame_digest.py', actual_file_name)
        assert_true(actual_lineno)