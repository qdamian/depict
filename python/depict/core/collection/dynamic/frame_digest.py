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

import os

class FrameDigest(object):
    '''
    Summarized information of a frame object.

    Used for easy access to the properties of a Frame object passed by the
    system's tracer.
    '''

    def __init__(self, frame):
        # Not storing the frame as an attribute to allow its garbage collection
        self.module_name = frame.f_globals['__name__']
        self.function_name = frame.f_code.co_name
        self.line_number = frame.f_lineno
        self._file_name = frame.f_code.co_filename

    @property
    def file_name(self):
        return os.path.abspath(self._file_name)
