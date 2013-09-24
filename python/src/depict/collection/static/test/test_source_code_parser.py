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

from mock import patch, Mock, ANY
from nose.tools import assert_true, assert_false
import unittest
from depict.collection.static.source_code_parser import SourceCodeParser

class TestSourceCodeParser(unittest.TestCase):

    def setUp(self):
        self.ast_ng_manager_patcher = patch('depict.collection.static.source_code_parser.ASTNGManager')
        self.ast_ng_manager_mock = Mock()
        self.ast_ng_manager_class_mock = self.ast_ng_manager_patcher.start()
        self.ast_ng_manager_class_mock.return_value = self.ast_ng_manager_mock

    def tearDown(self):
        self.ast_ng_manager_patcher.stop()

    def test_adds_base_path_to_top_of_python_path(self):
        with patch('depict.collection.static.source_code_parser.sys') as sys_mock:
            source_code_parser = SourceCodeParser('fake_base_path')
            sys_mock.path.insert.assert_called_once_with(0, 'fake_base_path')

    def test_creates_project_from_file_paths(self):
        file_paths = ['path/to/a.py', 'path/to/b.py']
        source_code_parser = SourceCodeParser('.')
        source_code_parser.add_files(file_paths)
        source_code_parser.parse()
        self.ast_ng_manager_mock.project_from_files.assert_called_once_with(file_paths, func_wrapper=ANY)

    def test_add_files_accepts_a_single_file(self):
        file_path = 'path/to/a/single/file.py'
        source_code_parser = SourceCodeParser('.')
        source_code_parser.add_files(file_path)
        source_code_parser.parse()
        self.ast_ng_manager_mock.project_from_files.assert_called_once_with([file_path], func_wrapper=ANY)

    def test_visits_defs_then_relations(self):
        with patch('depict.collection.static.source_code_parser.DefsVisitor') as defs_visitor_class_mock:
            with patch('depict.collection.static.source_code_parser.RelationsVisitor') as relations_visitor_class_mock:
                defs_visitor_mock = Mock()
                defs_visitor_class_mock.return_value = defs_visitor_mock
                relations_visitor_mock = Mock()
                relations_visitor_class_mock.return_value = relations_visitor_mock
                source_code_parser = SourceCodeParser('.')
                source_code_parser.add_files('dummy/path.py')
                source_code_parser.parse()
                defs_visitor_mock.visit.assert_called_once_with(ANY)
                relations_visitor_mock.visit.assert_called_once_with(ANY)

    def test_add_files_returns_true_if_at_least_one_file_was_added(self):
        paths1 = ['path/to/a.py', 'path/to/b.py']
        paths2 = ['path/to/b.py', 'path/to/c.py']
        source_code_parser = SourceCodeParser('.')
        source_code_parser.add_files(paths1)

        result = source_code_parser.add_files(paths2)

        assert_true(result)

    def test_add_files_returns_false_no_file_was_added(self):
        paths1 = ['path/to/a.py', 'path/to/b.py']
        paths2 = ['path/to/b.py']
        source_code_parser = SourceCodeParser('.')
        source_code_parser.add_files(paths1)

        result = source_code_parser.add_files(paths2)

        assert_false(result)
