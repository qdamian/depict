from depict.collection.dynamic.thread_scoped_tracer import ThreadScopedTracer
from depict.collection.dynamic import frame_digest

class FunctionList(object):
    def __init__(self, file_name):
        self.tracer = None
        self.out_file = open(file_name, 'w')
        
    def start(self):
        self.tracer = ThreadScopedTracer(self)
        self.tracer.start()
        
    def stop(self):
        self.tracer.stop()
        
    def on_call(self, frame_digest):
        self.out_file.write(frame_digest.function_name + '\n')
        
    def on_return(self, frame_digest):
        pass