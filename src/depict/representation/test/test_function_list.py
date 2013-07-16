from mock import Mock, MagicMock, call, ANY, patch, mock_open, PropertyMock
from depict.representation.function_list import FunctionList
from depict.collection.dynamic.frame_digest import FrameDigest

@patch('depict.representation.function_list.open', create=True)
class TestFunctionList():
    def test_init_opens_output_file(self, open_mock):
        FunctionList('file_name')
        open_mock.assert_called_once_with('file_name', 'w')

    def test_start_creates_thread_scoped_tracer(self, open_mock):
        with patch('depict.representation.function_list.ThreadScopedTracer') as tracer_class_mock:
            tracer_mock = Mock()
            tracer_class_mock.return_value = tracer_mock
            function_list = FunctionList('dummy_filename')
            function_list.start()
            tracer_class_mock.assert_called_once_with(function_list)
            tracer_mock.start.assert_called_once_with()

    def test_stop_stops_thread_scoped_tracer(self, open_mock):
        with patch('depict.representation.function_list.ThreadScopedTracer') as tracer_class_mock:
            tracer_mock = Mock()
            tracer_class_mock.return_value = tracer_mock
            function_list = FunctionList('dummy_filename')
            function_list.start()
            function_list.stop()
            tracer_mock.stop.assert_called_once_with()

    def test_stores_function_name_for_each_call(self, open_mock):
        file_mock = Mock()
        open_mock.return_value = file_mock
        function_list = FunctionList('dummy_filename')
        frame_digest_mock = Mock()
        type(frame_digest_mock).function_name = PropertyMock(return_value='fake_function1')
        function_list.on_call(frame_digest_mock)
        file_mock.write.assert_called_once_with('fake_function1\n')

    def test_ignores_notifications_of_call_return(self, open_mock):
        file_mock = Mock()
        open_mock.return_value = file_mock
        function_list = FunctionList('dummy_filename')
        frame_digest_mock = Mock()
        type(frame_digest_mock).function_name = PropertyMock(return_value='fake_function1')
        function_list.on_return(frame_digest_mock)
