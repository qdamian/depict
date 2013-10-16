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

from depict.core.collection.dynamic.frame_digest import FrameDigest


def _get_filename_without_extension(filepath):
    base = os.path.basename(filepath)
    return os.path.splitext(base)[0]

class ThreadScopedTracer(object):
    '''
    Trace function calls & returns using the system's trace function and notify
    each of these events to a 'call handler'. A call handler may be an object
    that knows how to process these events (e.g. creating an entity in the
    data model) or may be a filter object that chooses to forward or discard
    them.
    '''
    def __init__(self, call_handler):
        self.call_handler = call_handler
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
        trace_in_scope = self._process(event, frame)

        # Returning None means turn off tracing in the current scope
        if trace_in_scope:
            return self._trace_dispatcher
        else:
            return None

    def _process(self, event, frame):
        trace_in_scope = True
        if event == 'call':
            trace_in_scope = self._on_call(frame)
        elif event == 'return':
            trace_in_scope = self._on_return(frame)

        return trace_in_scope

    def _on_call(self, frame):
        frame_digest = FrameDigest(frame)
        if frame_digest.function_name == '__stop_trace__':
            return

        try:
            return self.call_handler.on_call(frame_digest)
        except AttributeError:
            pass

    def _on_return(self, frame):
        try:
            return self.call_handler.on_return(FrameDigest(frame))
        except AttributeError:
            pass
