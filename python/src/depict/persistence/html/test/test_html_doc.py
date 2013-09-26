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

from depict.persistence.html.html_doc import HtmlDoc
from mock import patch, mock_open
import unittest
from depict.model.entity.module import Module

class TestHtmlDoc(unittest.TestCase):

    def test_render_creates_html_doc(self):
        with patch('depict.persistence.html.html_doc.open', mock=mock_open, create=True) as open_mock:
            html_doc = HtmlDoc('fake_title', 'fake_filename')
            html_doc.render()
            open_mock.assert_called_once_with('fake_filename', 'w')

    def test_html_doc_title(self):
        open_mock = mock_open()
        with patch('depict.persistence.html.html_doc.open', open_mock, create=True):
            html_doc = HtmlDoc('fake_title', 'fake_filename')
            html_doc.render()
            handle = open_mock()
            self.assertTrue('<title>fake_title</title>' in handle.write.call_args[0][0])

    def test_outputs_module_names(self):
        open_mock = mock_open()
        with patch('depict.persistence.html.html_doc.open', open_mock, create=True):
            html_doc = HtmlDoc('dummy_title', 'dummy_filename')
            fake_module1 = Module('fake_module_id1', 'fake_module_name1')
            fake_module2 = Module('fake_module_id2', 'fake_module_name2')
            html_doc.on_module(fake_module1)
            html_doc.on_module(fake_module2)
            html_doc.render()
            handle = open_mock()
            actual_file_content = handle.write.call_args[0][0]
            self.assertTrue('<li>fake_module_name1</li>' in actual_file_content)
            self.assertTrue('<li>fake_module_name2</li>' in actual_file_content)

    def test_html_has_header_and_footer(self):
        open_mock = mock_open()
        with patch('depict.persistence.html.html_doc.open', open_mock, create=True):
            html_doc = HtmlDoc('dummy_title', 'dummy_filename')
            html_doc.render()
            handle = open_mock()
            self.assertTrue('<ul>' in handle.write.call_args[0][0])
            self.assertTrue('</ul>' in handle.write.call_args[0][0])