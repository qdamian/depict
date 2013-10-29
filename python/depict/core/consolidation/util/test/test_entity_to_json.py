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

import json
from nose.tools import *
from mock import patch, ANY
from depict.core.consolidation.util.entity_to_json import EntityToJson
from depict.core.model.entity.entity import Entity


class SimpleObject(object):
    __metaclass__ = Entity

    def __init__(self, id_ = 'fake_id', name = 'fake_name'):
        self.id_ = id_
        self.name = name

def assert_equal_json(a, b):
    normalize = lambda json_str: json.dumps(json.loads(json_str))
    assert_equal(normalize(a), normalize(b))

class TestEntityToJson(object):
    def test_serialize_simple_object_returns_json_with_its_attributes(self):
        obj = SimpleObject()

        actual_json = EntityToJson.convert(obj, 'id_')

        actual_data = json.loads(actual_json)
        assert_equal(actual_data['id_'], 'fake_id')
        assert_equal(actual_data['name'], 'fake_name')

    def test_serialize_includes_an_element_with_the_type_of_object(self):
        obj = SimpleObject()

        actual_json = EntityToJson.convert(obj, 'id_')

        actual_data = json.loads(actual_json)
        assert_equal(actual_data['type'], 'SimpleObject')

    def test_serialize_handles_references_to_other_objects(self):
        obj1 = SimpleObject('id1', 'name1')
        obj2 = SimpleObject('id2', 'name2')
        obj2.some_reference = obj1

        actual_json = EntityToJson.convert(obj2, 'id_')

        actual_data = json.loads(actual_json)
        assert_in('some_reference', actual_data)
        reference = actual_data['some_reference']
        assert_equal(len(reference), 2)
        assert_equal(reference['type'], 'SimpleObject')
        assert_equal(reference['id_'], 'id1')

    def test_serializes_handles_multiple_references(self):
        obj1 = SimpleObject('id1', 'name1')
        obj2 = SimpleObject('id2', 'name2')
        obj3 = SimpleObject('id3', 'name2')
        obj3.points_to = [obj1, obj2]

        actual_json = EntityToJson.convert(obj3, 'id_')

        actual_data = json.loads(actual_json)
        ref = actual_data['points_to']
        assert_equal(['id1', 'id2'], [ref[0]['id_'], ref[1]['id_']])

    def test_serialize_formats_the_output(self):
        obj = SimpleObject('fake_id', 'fake_name')
        with patch('depict.core.consolidation.util.entity_to_json.dumps') as dumps_mock:
            actual_json = EntityToJson.convert(obj, 'key')
            dumps_mock.assert_called_once_with(ANY, cls=ANY, indent=4, separators=(',',':'))