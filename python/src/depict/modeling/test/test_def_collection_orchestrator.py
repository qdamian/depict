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

from depict.modeling.def_collection_orchestrator import DefCollectionOrchestator
from depict.modeling.def_collection_orchestrator import AlreadyProcessed
from mock import Mock, patch, ANY
from nose.tools import assert_raises
import unittest

@patch('depict.modeling.def_collection_orchestrator.EntityIdGenerator')
@patch('depict.modeling.def_collection_orchestrator.SourceCodeParser')
class TestDefCollectionOrchestrator(unittest.TestCase):
    def setUp(self):
        self.fake_collector = Mock()
        self.fake_collector_class = Mock(return_value=self.fake_collector)

    def test_creates_included_collectors(self, dummy1, dummy2):
        def_collection_orchestrator = DefCollectionOrchestator('.')

        def_collection_orchestrator.include(self.fake_collector_class)
        def_collection_orchestrator.process('fake_file_name')

        self.fake_collector_class.assert_called_once_with(ANY, ANY)

    def test_process_raises_already_processed_if_all_files_had_been_processed(self, source_code_parser_class_mock, entity_id_generator_class_mock):
        source_code_parser_mock = Mock()
        source_code_parser_mock.add_files.side_effect = [True, False]
        source_code_parser_class_mock.return_value = source_code_parser_mock
        def_collection_orchestrator = DefCollectionOrchestator('.')

        def_collection_orchestrator.include(self.fake_collector_class)
        def_collection_orchestrator.process('fake_file_name')

        assert_raises(AlreadyProcessed, def_collection_orchestrator.process, 'fake_file_name')
