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
from mock import patch, ANY, Mock
from nose.tools import assert_is_instance, assert_equal, assert_raises
from nose_parameterized import parameterized

from depict.core.consolidation.util.json_to_entity import JsonToEntity
from depict.core.model.entity.function import Function
from depict.core.model.entity.module import Module
from depict.core.model.entity.thread import Thread
from depict.core.consolidation.util.entity_to_json import EntityToJson
from depict.test.object_factory import real, unique
from depict.core.consolidation.util.test.test_entity_to_json import SimpleObject


class TestJsonDeserializer():
    @parameterized.expand([('',), ('{not json}'), (None,)])
    def test_it_raises_a_value_exception_if_the_argument_is_not_valid_json(self, invalid_json):
        # Arrange nothing
        # Act & assert
        assert_raises(ValueError, JsonToEntity().convert, invalid_json)

    def test_it_deserializes_a_simple_object(self):
        # Arrange
        json_data = '{"id_": "simple_id", "type": "SimpleObject", "name": "example"}'

        # Act
        obj = JsonToEntity().convert(json_data)

        # Assert
        assert_is_instance(obj, SimpleObject)
        assert_equal(obj.id_, 'simple_id')
        assert_equal(obj.name, 'example')

    def test_it_raises_a_value_exception_if_object_type_is_unknown(self):
        # Arrange
        json_data = '{"id_": "simple_id", "type": "UnknownObject", "name": "example"}'

        # Act & assert
        assert_raises(ValueError, JsonToEntity().convert, json_data)

    def test_it_works_on_a_real_entity_object(self):
        # Arrange
        expected_module = real('Module')
        expected_function = real('Function')
        json_module = EntityToJson.convert(expected_module, 'id_')
        json_function = EntityToJson.convert(expected_function, 'id_')
        json_to_entity = JsonToEntity()

        # Act
        actual_thread = json_to_entity.convert(json_module)
        actual_function = json_to_entity.convert(json_function)

        # Assert
        assert_is_instance(actual_thread, Module)
        assert_equal(actual_thread, expected_module)
        assert_is_instance(actual_function, Function)
        assert_equal(actual_function, expected_function)

    def test_it_revives_one_reference(self):
        # Arrange
        expected_module = real('Module')
        expected_function = real('Function')
        json_module = EntityToJson.convert(expected_module, 'id_')
        json_function = EntityToJson.convert(expected_function, 'id_')
        json_to_entity = JsonToEntity()

        # Act
        actual_module = json_to_entity.convert(json_module)
        actual_function = json_to_entity.convert(json_function)

        # Assert
        assert_is_instance(actual_function, Function)
        assert_is_instance(actual_function.parent, Module)
        assert_equal(actual_function.parent, actual_module)

    def test_it_logs_an_exception_if_an_invalid_reference_is_found(self):
            # Arrange
            module1 = unique(real('Module'))
            module2 = unique(real('Module'))
            function = real('Function')
            function.parent = module1
            json_module2 = EntityToJson.convert(module2, 'id_')
            json_function = EntityToJson.convert(function, 'id_')
            json_to_entity = JsonToEntity()
            json_to_entity.logger = Mock()

            # Act
            json_to_entity.convert(json_module2)

            assert_raises(KeyError, json_to_entity.convert, json_function)

            json_to_entity.logger.exception.assert_called_once_with(ANY, ANY, ANY)
