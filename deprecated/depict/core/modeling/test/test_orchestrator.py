#region GPLv3 notice
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
#endregion

from mock import Mock, patch, ANY
from nose.tools import *

from depict.core.modeling.orchestrator import Orchestrator
from depict.core.modeling.orchestrator import AlreadyProcessed
from depict.test.object_factory import fake


@patch('depict.core.modeling.orchestrator.EntityIdGenerator', autospec=True)
@patch('depict.core.modeling.orchestrator.SourceCodeParser', autospec=True)
class TestOrchestrator():
    def setUp(self):
        self.generic_modeler_class = Mock()

    def test_it_creates_the_included_modelers(self, _, __):
        # Arrange
        orchestrator = Orchestrator(fake('base_path'), fake('Model'))

        # Act
        orchestrator.include(self.generic_modeler_class)
        orchestrator.process('file_name')

        # Assert
        self.generic_modeler_class.assert_called_once_with(ANY, ANY, ANY)

    def test_process_raises_exception_if_all_files_had_been_processed(self,
                                              source_code_parser_class_mock,
                                              _):
        # Arrange
        source_code_parser_mock = fake('SourceCodeParser')
        source_code_parser_mock.add_files.side_effect = [True, False]
        source_code_parser_class_mock.return_value = source_code_parser_mock
        orchestrator = Orchestrator(fake('base_path'), fake('Model'))

        # Act
        orchestrator.include(self.generic_modeler_class)
        orchestrator.process('file_name')

        # Assert
        assert_raises(AlreadyProcessed, orchestrator.process, 'file_name')