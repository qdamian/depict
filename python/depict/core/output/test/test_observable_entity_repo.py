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

from nose_parameterized import parameterized
from nose.tools import assert_equal
from mock import Mock

from depict.core.output.observable_entity_repo import ObservableEntityRepo
from depict.test.template import real


class TestObservableEntityRepo():

    @parameterized.expand([('Module',),
                           ('Class_',),
                           ('Function',),
                           ('Thread',),
                           ('FunctionCall',)])
    def test_add_still_works(self, entity_class):
        # Arrange
        observable_repo = ObservableEntityRepo(Mock())
        entity = real(entity_class)

        # Act
        observable_repo.add(entity)

        # Assert
        assert_equal(observable_repo.get_by_id(entity.id_), entity)

    @parameterized.expand([('Module'),
                           ('Class_'),
                           ('Function'),
                           ('Thread'),
                           ('FunctionCall')])
    def test_it_notifies_when_one_entity_is_added(self, entity_class):
        # Arrange
        observer = Mock()
        repo = ObservableEntityRepo(observer)
        entity = real(entity_class)

        # Act
        repo.add(entity)

        # Assert
        observer.on_entity.assert_called_once_with(entity)
