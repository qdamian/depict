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

from depict.collection.dynamic.frame_digest import FrameDigest
from depict.model.entity.class_ import Class_
from depict.output.toy.def_list import DefList
from depict.test.template import real
from mock import Mock, MagicMock, call, ANY, patch, mock_open, PropertyMock
from nose.tools import assert_true

@patch('depict.output.toy.def_list.open', create=True)
class TestDefList():
    def setUp(self):
        self.file_set_mock = MagicMock()
        self.file_set_mock.directory = '.'

    def test_init_opens_output_file(self, open_mock):
        DefList(self.file_set_mock, 'mock_output_file_name')
        open_mock.assert_called_once_with('mock_output_file_name', 'w')

    def test_init_creates_static_data_notifier(self, open_mock):
        with patch('depict.output.toy.def_list.StaticDataNotifier') as static_data_notifier_mock:
            fileset_mock = MagicMock()
            def_list = DefList(fileset_mock, 'dummy_filename')
            static_data_notifier_mock.assert_called_once_with(fileset_mock, def_list, ANY)

    def test_runs_static_def_notifier(self, open_mock):
        def_list = DefList(self.file_set_mock, 'dummy_filename')
        def_list.static_data_notifier = Mock()
        def_list.run()
        def_list.static_data_notifier.run.assert_called_once_with()

    def test_stores_function_name_for_each_function(self, open_mock):
        file_mock = Mock()
        open_mock.return_value = file_mock
        def_list = DefList(self.file_set_mock, 'dummy_filename')
        fake_function = real('Function')
        def_list.on_function(fake_function)
        expected_call = call('%s\n' % fake_function.name)
        assert_true(expected_call in file_mock.write.mock_calls)

    def test_stores_class_name_for_each_class(self, open_mock):
        file_mock = Mock()
        open_mock.return_value = file_mock
        def_list = DefList(self.file_set_mock, 'dummy_filename')
        fake_class = real('Class_')
        def_list.on_class(fake_class)
        expected_call = call('%s\n' % fake_class.name)
        assert_true(expected_call in file_mock.write.mock_calls)
