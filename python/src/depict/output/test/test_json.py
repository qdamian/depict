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

from depict.output.json import Json
from mock import patch, MagicMock, Mock, ANY
import unittest

@patch('depict.output.json.StaticDataNotifier', autospec=True)
@patch('depict.output.json.JsonDoc', autospec=True)
class TestJson(unittest.TestCase):

    def test_can_be_created(self, json_doc_class_mock, static_data_class_mock):
        fileset_mock = Mock()
        Json(fileset_mock, 'dummy_out_file')

    def test_runs_static_def_notifier(self, json_doc_class_mock, static_data_class_mock):
        static_data_mock = Mock()
        static_data_class_mock.return_value = static_data_mock
        json = Json(MagicMock(), 'dummy_out_file')
        json.run()
        static_data_mock.run.assert_called_once_with()

    def test_generates_json_output(self, json_doc_class_mock, static_data_class_mock):
        json_doc_mock = Mock()
        json_doc_class_mock.return_value = json_doc_mock
        json = Json(MagicMock(), 'dummy_out_file')
        json.run()
        json_doc_mock.generate.assert_called_once_with()
