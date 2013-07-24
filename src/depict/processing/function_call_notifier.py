from depict.collection.dynamic.thread_scoped_tracer import ThreadScopedTracer
from depict.processing.class_definition_locator import ClassDefinitionLocator
from depict.processing.function_definition_locator import \
                                                       FunctionDefinitionLocator
from depict.model.function_call import FunctionCall
from depict.processing.static_data_collector import GlobalStaticDataCollector

class FunctionCallNotifier():
    def __init__(self, observer):
        self.thread_scoped_tracer = ThreadScopedTracer(self)
        self.observer = observer
        GlobalStaticDataCollector.include(ClassDefinitionLocator)
        GlobalStaticDataCollector.include(FunctionDefinitionLocator)
        self.stop = self.thread_scoped_tracer.stop

    def start(self):
        self.thread_scoped_tracer.start()
        
    def on_call(self, frame_digest):
        function_id = (frame_digest.file_name + ':' +
                       str(frame_digest.line_number))
        GlobalStaticDataCollector.process(frame_digest.file_name)
        self.observer.on_call(FunctionCall(function_id))
