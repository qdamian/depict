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

from depict.modeling.def_collection_orchestrator import DefCollectionOrchestator
from depict.output.json import Json
from formic.formic import FileSet

if __name__ == '__main__':
    base_path = '/usr/local/lib/python2.7/dist-packages/pyasteroids'
    file_set = FileSet(directory=base_path, include='*.py')

    json = Json(file_set, 'pyasteroids.json')

    json.run()
