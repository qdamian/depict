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

from depict.processing.static_data_notifier import StaticDataNotifier
from formic.formic import FileSet
from functools import wraps

def count_calls(func):
    func.call_count = 0
    @wraps(func)
    def wrapper(*args):
        func.call_count += 1
        args = args + (func.call_count,)
        return func(*args)
    return wrapper

class DefinitionList(object):

    def __init__(self, input_glob, output_filename):
        self.out_file = open(output_filename, 'w')
        file_set = FileSet(input_glob)
        file_names = [name for name in file_set]
        self.static_data_notifier = StaticDataNotifier(file_names, self)

    def run(self):
        self.static_data_notifier.run()

    @count_calls
    def on_class(self, class_, call_count):
        if call_count == 1:
            self.out_file.write('\n*Classes*\n\n')

        self.out_file.write(class_.name + '\n')

    @count_calls
    def on_function(self, function, call_count):
        if call_count == 1:
            self.out_file.write('\n*Functions*\n\n')

        try:
            self.out_file.write(function.Class_.name + '.')
        except AttributeError:
            pass
        self.out_file.write(function.name + '\n')
