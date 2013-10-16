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

import os
import sys


class ProgramEnvEmulator(object):

    def __init__(self, argv):
        program_name = argv[1]
        self.globals = { '__file__': program_name,
                         '__name__': '__main__',
                         '__package__': None,
                         '__cached__': None
                        }

        self.base_path = os.path.dirname(os.path.abspath(program_name))
        sys.path = [self.base_path] + sys.path

        with open(program_name, 'r') as program_file:
            self.code = compile(program_file.read(), program_name, 'exec')
