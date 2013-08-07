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

import os

class FrameDigest(object):
    '''Summary of a frame object'''

    def __init__(self, frame):
        self.frame = frame

    @property
    def function_name(self):
        return self.frame.f_code.co_name

    @property
    def module_name(self):
        return self.frame.f_globals['__name__']

    @property
    def file_name(self):
        return os.path.abspath(self.frame.f_code.co_filename)

    @property
    def line_number(self):
        return self.frame.f_lineno
