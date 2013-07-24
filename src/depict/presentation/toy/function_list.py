from depict.collection.dynamic.thread_scoped_tracer import ThreadScopedTracer
from depict.processing.function_call_notifier import FunctionCallNotifier
from depict.collection.dynamic import frame_digest

class FunctionList(object):
    def __init__(self, file_name):
        self.out_file = open(file_name, 'w')
        self.function_call_notifier = FunctionCallNotifier(self)
        self.stop = self.function_call_notifier.stop
            
    def start(self):
        self.function_call_notifier.start()
   
    def on_call(self, function_call):
        try:
            self.out_file.write(function_call.function.Class_.name + '.')
        except AttributeError:
            pass
        self.out_file.write(function_call.function.name + '\n')
