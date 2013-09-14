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

from json import loads, dumps, JSONEncoder

# pylint:disable = method-hidden
class ReferenceEncoder(JSONEncoder):
    def default(self, obj):
        if not type(obj) in [int, str, list, dict]:
            return {'type': type(obj).__name__,
                    self.key: getattr(obj, self.key)}
        return JSONEncoder.default(self, obj)

# pylint:disable = method-hidden
class ObjectEncoder(JSONEncoder):
    def default(self, obj):
        values = obj.__dict__
        values['type'] = type(obj).__name__
        encoder = ReferenceEncoder
        encoder.key = self.key
        return loads(dumps(values, cls=ReferenceEncoder))

# pylint:disable = too-few-public-methods
class JsonSerializer(object):
    @staticmethod
    def serialize(obj, key):
        encoder = ObjectEncoder
        encoder.key = key
        return dumps(obj, cls=encoder, indent=4, separators=(',',':'))
