#region GPLv3 notice
# Copyright 2014 Damian Quiroga
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

from dissect.model.entity.function import Function
from mock import patch, ANY, Mock

from depict.data.retriever import Retriever


@patch('depict.data.retriever.dissect', autospec=True)
class TestRetriever(object):
    def test_it_runs_dissect_on_the_file(self, dissect):
        # Arrange
        retriever = Retriever("fake/file", Mock())

        # Act
        retriever.run()

        # Assert
        dissect.run.assert_called_once_with("fake/file", ANY)


    @patch('depict.data.retriever.EntityToJson')
    def test_it_converts_each_entity_to_json(self, entity2json, dissect):
        # Arrange
        retriever = Retriever("dummy/file", Mock())
        function = Function(id_='func1', name='function1')

        # Act
        retriever.on_entity(function)

        # Assert
        entity2json.convert.assert_called_once_with(function, 'id_')

    @patch('depict.data.retriever.EntityToJson')
    def test_it_calls_back_with_each_entity_in_json(self, entity2json, dissect):
        # Arrange
        callback = Mock()
        retriever = Retriever("dummy/file", callback)
        function = Function(id_='func1', name='function1')
        entity2json.convert.return_value = 'fake json'

        # Act
        retriever.on_entity(function)

        # Assert
        callback.assert_called_once_with('fake json')
