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

from depict.model.model import Model
from depict.modeling.static_data_notifier import StaticDataNotifier
from formic.formic import FileSet

def get_all_modules(file_set):
    model = Model()
    StaticDataNotifier(file_set, None, model).run()
    return model.modules.get_all()

def get_representations(base_path):
    repr_dir = FileSet(directory=base_path, include='depict/txt/**')
    return get_all_modules(repr_dir)
