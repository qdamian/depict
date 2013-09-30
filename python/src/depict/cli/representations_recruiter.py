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

from depict.modeling.static_data_notifier import StaticDataNotifier
from formic.formic import FileSet
import importlib
from depict.model.model import Model

def get_repr_description(mod_name):
    imported_mod = importlib.import_module(mod_name + '.profile')
    return imported_mod.DESCRIPTION

def get_repr_module_names(file_set):
    model = Model()
    StaticDataNotifier(file_set, None, model).run()
    return [mod.name for mod in model.modules.get_all()]

# pylint:disable = too-few-public-methods
class RepresentationsRecruiter(object):
    def __init__(self, base_path):
        self.file_set = FileSet(directory=base_path,
                                include=['depict/txt/**',
                                         'depict/html5/**'])

    def run(self):
        mod_names = get_repr_module_names(self.file_set)
        repr_desc = []
        for name in mod_names:
            try:
                repr_desc.append((name, get_repr_description(name)))
            except ImportError:
                pass
        repr_desc.sort()
        return repr_desc