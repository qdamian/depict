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

from mock import Mock, MagicMock, call, ANY, patch, mock_open, PropertyMock
from depict.output.toy.function_call_list import FunctionCallList
from depict.collection.dynamic.frame_digest import FrameDigest
from depict.model.function_call import FunctionCall
from depict.model.function import Function
import unittest

@patch('depict.output.toy.function_call_list.open', create=True)
class TestFunctionCallList(unittest.TestCase):
    def test_init_opens_output_file(self, open_mock):
        FunctionCallList('file_name', '.')
        open_mock.assert_called_once_with('file_name', 'w')

    def test_init_creates_function_call_notifier(self, open_mock):
        with patch('depict.output.toy.function_call_list.FunctionCallNotifier') as function_call_notifier_class_mock:
            function_call_list = FunctionCallList('file_name', '.')
            function_call_notifier_class_mock.assert_called_once_with(function_call_list, ANY, ANY)

    def test_starts_function_call_notifier(self, open_mock):
        function_call_list = FunctionCallList('file_name', '.')
        function_call_list.function_call_notifier = Mock()
        function_call_list.start()
        function_call_list.function_call_notifier.start.assert_called_once_with()

    def test_stops_function_call_notifier(self, open_mock):
        call_notifier_mock = Mock()
        call_notifier_class_mock = Mock(return_value=call_notifier_mock)
        with patch('depict.output.toy.function_call_list.FunctionCallNotifier', call_notifier_class_mock):
            function_call_list = FunctionCallList('file_name', '.')
            function_call_list.start()
            function_call_list.stop()
            call_notifier_mock.stop.assert_called_once_with()

    def test_stores_function_name_for_each_call(self, open_mock):
        file_mock = Mock()
        open_mock.return_value = file_mock
        function_call_list = FunctionCallList('dummy_filename', '.')
        function_call_mock = Mock()
        fake_function = Function('fake_id', 'fake_name')
        function_mock = PropertyMock(return_value=fake_function)
        type(function_call_mock).function = function_mock
        function_call_list.on_call(function_call_mock)
        file_mock.write.assert_called_once_with('fake_name\n')

