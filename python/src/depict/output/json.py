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

from depict.persistence.json.json_doc import JsonDoc
from depict.modeling.static_data_notifier import StaticDataNotifier

# pylint: disable=R0903
class Json(object):

    def __init__(self, file_set, out_filename):
        self.json_doc = JsonDoc(out_filename)
        file_names = [name for name in file_set]
        self.static_data_notifier = StaticDataNotifier(file_names,
                                                       self.json_doc)

    def run(self):
        self.static_data_notifier.run()
