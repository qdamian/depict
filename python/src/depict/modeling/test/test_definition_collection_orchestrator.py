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

from depict.modeling.definition_collection_orchestrator import \
                                                DefinitionCollectionOrchestrator
from mock import Mock, patch
import unittest

@patch('depict.modeling.definition_collection_orchestrator.GlobalSourceCodeParser')
class TestDefinitionCollectionOrchestrator(unittest.TestCase):

    def test_include_stores_collector(self, source_code_parser_mock):
        fake_collector = Mock()
        fake_collector_class = Mock(return_value=fake_collector)
        def_collection_orchestrator = DefinitionCollectionOrchestrator()
        def_collection_orchestrator.include(fake_collector_class)
        def_collection_orchestrator.process('fake_file_name')
        fake_collector_class.assert_called_once_with()

    def test_passes_base_path_to_source_code_parser(self, source_code_parser_mock):
        def_collection_orchestrator = DefinitionCollectionOrchestrator()
        def_collection_orchestrator.set_base_path('fake/base/path')
        source_code_parser_mock.set_base_path.assert_called_once_with('fake/base/path')