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

import dissect
from dissect.consolidation.util.entity_to_json import EntityToJson


class Retriever(object):
    def __init__(self, filepath, callback):
        self.filepath = filepath
        self.callback = callback

    def run(self):
        dissect.run(self.filepath, self.on_entity)

    def on_entity(self, entity):
        self.callback(EntityToJson.convert(entity, 'id_'))