import sys
import os
from depict.collection.dynamic.frame_digest import FrameDigest

def _get_filename_without_extension(filepath):
    base = os.path.basename(filepath)
    return os.path.splitext(base)[0]

class ThreadScopedTracer(object):
    '''
    Trace function calls & returns using the system's trace function.

    Somewhat similar to trace.Trace or bdb.Bdb but with responsibility limited
    to dispatching based on event type.
    '''
    def __init__(self, observer):
        self.observer = observer
        self.filename = _get_filename_without_extension(__file__)

    def start(self):
        sys.settrace(self._trace_dispatcher)

    def stop(self):
        sys.settrace(None)

    def _trace_dispatcher(self, frame, event, arg):
        if self._calling_ourselves(frame):
            return

        if event == 'call':
            self._on_call(frame)
        elif event == 'return':
            self._on_return(frame)
        return self._trace_dispatcher

    def _calling_ourselves(self, frame):
        event_filename = _get_filename_without_extension(
                                                     frame.f_code.co_filename)
        return event_filename == self.filename

    def _on_call(self, frame):
        self.observer.on_call(FrameDigest(frame))

    def _on_return(self, frame):
        self.observer.on_return(FrameDigest(frame))
