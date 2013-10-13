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

from depict.core.modeling.def_collection_orchestrator import DefCollectionOrchestator
from depict.core.modeling.def_collection_orchestrator import AlreadyProcessed
from mock import Mock, patch, ANY
from nose.tools import *
from depict.test.template import fake

@patch('depict.core.modeling.def_collection_orchestrator.EntityIdGenerator', autospec=True)
@patch('depict.core.modeling.def_collection_orchestrator.SourceCodeParser', autospec=True)
class TestDefCollectionOrchestrator():
    def setUp(self):
        self.generic_collector_class = Mock()

    def test_it_creates_the_included_collectors(self, _, __):
        # Arrange
        def_collection_orchestrator = DefCollectionOrchestator(fake('base_path'),
                                                               fake('Model'))

        # Act
        def_collection_orchestrator.include(self.generic_collector_class)
        def_collection_orchestrator.process('file_name')

        # Assert
        self.generic_collector_class.assert_called_once_with(ANY, ANY, ANY)

    def test_process_raises_exception_if_all_files_had_been_processed(self,
                                              source_code_parser_class_mock,
                                              entity_id_generator_class_mock):
        # Arrange
        source_code_parser_mock = fake('SourceCodeParser')
        source_code_parser_mock.add_files.side_effect = [True, False]
        source_code_parser_class_mock.return_value = source_code_parser_mock
        def_collection_orchestrator = DefCollectionOrchestator(fake('base_path'),
                                                               fake('Model'))

        # Act
        def_collection_orchestrator.include(self.generic_collector_class)
        def_collection_orchestrator.process('file_name')

        # Assert
        assert_raises(AlreadyProcessed, def_collection_orchestrator.process, 'file_name')