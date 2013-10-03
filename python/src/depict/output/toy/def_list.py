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

from depict.modeling.static_data_notifier import StaticDataNotifier
from functools import wraps
from depict.model.model import Model

def count_calls(func):
    func.call_count = 0
    @wraps(func)
    def wrapper(*args):
        func.call_count += 1
        args = args + (func.call_count,)
        return func(*args)
    return wrapper

class DefList(object):

    def __init__(self, file_set, output_filename):
        self.out_file = open(output_filename, 'w')
        self.static_data_notifier = StaticDataNotifier(file_set, self, Model())

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
