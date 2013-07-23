from mock import Mock, MagicMock, call, ANY, patch, mock_open, PropertyMock
from depict.presentation.toy.function_list import FunctionList
from depict.collection.dynamic.frame_digest import FrameDigest
from depict.model.function_call import FunctionCall
from depict.model.function import Function

@patch('depict.presentation.toy.function_list.open', create=True)
class TestFunctionList():
    def test_init_opens_output_file(self, open_mock):
        FunctionList('file_name')
        open_mock.assert_called_once_with('file_name', 'w')

    def test_init_createsFunctioncall_notifier(self, open_mock):
        with patch('depict.presentation.toy.function_list.FunctionCallNotifier') as function_call_notifierClass_mock:
            function_list = FunctionList('file_name')
            function_call_notifierClass_mock.assert_called_once_with(function_list)

    def test_startsFunctioncall_notifier(self, open_mock):
        function_list = FunctionList('file_name')
        function_list.function_call_notifier = Mock()
        function_list.start()
        function_list.function_call_notifier.start.assert_called_once_with()

    def test_stopsFunctioncall_notifier(self, open_mock):
        function_list = FunctionList('file_name')
        function_list.function_call_notifier = Mock()
        function_list.start()
        function_list.stop()
        function_list.function_call_notifier.stop.assert_called_once_with()

    def test_storesFunctionname_for_each_call(self, open_mock):
        file_mock = Mock()
        open_mock.return_value = file_mock
        function_list = FunctionList('dummy_filename')
        function_call_mock = Mock()
        fake_function = Function('fake_name', 'fake_id')
        function_mock = PropertyMock(return_value=fake_function)
        type(function_call_mock).function = function_mock
        function_list.on_call(function_call_mock)
        file_mock.write.assert_called_once_with('fake_name\n')
 
