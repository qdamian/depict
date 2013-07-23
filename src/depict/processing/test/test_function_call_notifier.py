from mock import Mock, patch, PropertyMock, ANY, mock_open, call
from depict.processing.function_call_notifier import FunctionCallNotifier
from depict.model.class_repo import GlobalClassRepo
from depict.model.function_repo import GlobalFunctionRepo
from depict.processing.class_definition_locator import ClassDefinitionLocator
from depict.processing.function_definition_locator import FunctionDefinitionLocator

class TestFunctionCallNotifier():
    def test_init_creates_thread_scoped_tracer(self):
        with patch('depict.processing.function_call_notifier.ThreadScopedTracer') as tracerClass_mock:
            tracer_mock = Mock()
            tracerClass_mock.return_value = tracer_mock
            function_call_notifier = FunctionCallNotifier(Mock())
            tracerClass_mock.assert_called_once_with(function_call_notifier)
    
    def test_start_creates_thread_scoped_tracer(self):
        with patch('depict.processing.function_call_notifier.ThreadScopedTracer') as tracerClass_mock:
            tracer_mock = Mock()
            tracerClass_mock.return_value = tracer_mock
            function_call_notifier = FunctionCallNotifier(Mock())
            function_call_notifier.start()
            tracer_mock.start.assert_called_once_with()

    def test_stop_stops_thread_scoped_tracer(self):
        with patch('depict.processing.function_call_notifier.ThreadScopedTracer') as tracerClass_mock:
            tracer_mock = Mock()
            tracerClass_mock.return_value = tracer_mock
            function_call_notifier = FunctionCallNotifier(Mock())
            function_call_notifier.start()
            function_call_notifier.stop()
            tracer_mock.stop.assert_called_once_with()

    def test_processes_static_data_for_each_call(self):
        with patch('depict.processing.function_call_notifier.GlobalStaticDataCollector') as global_static_data_collector_mock:
            observer_mock = Mock()
            function_call_notifier = FunctionCallNotifier(observer_mock)
            frame_digest_mock = Mock()
            type(frame_digest_mock).function_name = PropertyMock(return_value='fake_function_name')
            type(frame_digest_mock).file_name = PropertyMock(return_value='fake_file_name')
            type(frame_digest_mock).line_number = PropertyMock(return_value=1)
            function_call_notifier.on_call(frame_digest_mock)
            calls = [call(ClassDefinitionLocator), call(FunctionDefinitionLocator)]
            global_static_data_collector_mock.include.assert_has_calls(calls)
            global_static_data_collector_mock.process.assert_called_once_with('fake_file_name')
