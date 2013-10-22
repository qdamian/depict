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

import json
import logging
from depict.core.model.entity.entity import Entity


class JsonToEntity(object):
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.known_entities = {}

    def convert(self, json_serialized_object, id_='id_'):
        '''
        Raises KeyError if a reference is not found.
        '''
        obj_attr = self._get_object_attributes(json_serialized_object)
        self._revive_references(obj_attr, id_)
        entity_class = self._identify_object_class(obj_attr)
        entity = self._instantiate_entity(entity_class, obj_attr)
        if entity:
            self.known_entities[entity.id_] = entity
        return entity

    def _get_object_attributes(self, json_serialized_object):
        try:
            return json.loads(json_serialized_object)
        except TypeError:
            raise ValueError('%s is not a valid JSON string' %
                             json_serialized_object)

    def _identify_object_class(self, obj_attribute):
        try:
            return Entity.catalog[obj_attribute['type']]
        except KeyError:
            raise ValueError('%(type)s is not an entity type %(known_types)s' %
                             {'type': obj_attribute['type'],
                              'known_types': Entity.catalog})

    def _instantiate_entity(self, entity_class, obj_attribute):
        entity = entity_class()
        for attr in obj_attribute:
            setattr(entity, attr, obj_attribute[attr])
        return entity

    def _revive_references(self, obj, id_):
        for attr in obj:
            candidate = obj[attr]
            if isinstance(candidate, dict) and id_ in candidate:
                try:
                    referenced = self.known_entities[candidate[id_]]
                    obj[attr] = referenced
                except KeyError:
                    self.logger.exception('Could not find reference %s for %s',
                                          id_, obj)
                    raise
