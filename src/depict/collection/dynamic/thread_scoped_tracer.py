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

from depict.collection.dynamic.frame_digest import FrameDigest
import os
import sys

def _get_filename_without_extension(filepath):
    base = os.path.basename(filepath)
    return os.path.splitext(base)[0]

# pylint: disable=R0903
class ThreadScopedTracer(object):
    '''
    Trace function calls & returns using the system's trace function.

    Somewhat similar to trace.Trace or bdb.Bdb but with responsibility limited
    to dispatching based on event type.
    '''
    def __init__(self, observer):
        self.observer = observer
        self.filename = _get_filename_without_extension(__file__)
        self.stop = self.__stop_trace__
        self.running = False

    def start(self):
        sys.settrace(self._trace_dispatcher)
        self.running = True

    def __stop_trace__(self):
        sys.settrace(None)
        self.running = False

    def _trace_dispatcher(self, frame, event, _):
        if event == 'call':
            self._on_call(frame)
        elif event == 'return':
            self._on_return(frame)
        return self._trace_dispatcher

    def _on_call(self, frame):
        frame_digest = FrameDigest(frame)
        if frame_digest.function_name == '__stop_trace__':
            return
        
        try:
            self.observer.on_call(frame_digest)
        except AttributeError:
            pass

    def _on_return(self, frame):
        try:
            self.observer.on_return(FrameDigest(frame))
        except AttributeError:
            pass
