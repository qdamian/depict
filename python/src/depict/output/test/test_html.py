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

from depict.output.html import Html
from mock import patch, MagicMock, Mock, ANY
import unittest

class TestHtml(unittest.TestCase):

    def test_init_creates_static_data_notifier(self):
        with patch('depict.output.html.StaticDataNotifier') as static_data_notifier_mock:
            expected_paths = ['fake/file/a.py', 'file/file/b.py']
            fileset_mock = Mock()
            html = Html(fileset_mock, 'dummy_title', 'dummy_out_file')
            static_data_notifier_mock.assert_called_once_with(fileset_mock,
                                                              html.html_doc,
                                                              ANY)

    def test_init_creates_html_doc(self):
        with patch('depict.output.html.HtmlDoc') as html_doc_class_mock:
            dummy_file_set = Mock()
            dummy_file_set.directory = '.'
            Html(dummy_file_set, 'fake_title', 'fake_out_file')
            html_doc_class_mock.assert_called_once_with('fake_title', 'fake_out_file')

    def test_runs_static_def_notifier(self):
        with patch('depict.output.html.HtmlDoc') as html_doc_class_mock:
            file_set_mock = Mock()
            file_set_mock.directory = '.'
            html = Html(file_set_mock, 'dummy_title', 'dummy_out_file')
            html.static_data_notifier = Mock()
            html.run()
            html.static_data_notifier.run.assert_called_once_with()