from depict.collection.dynamic.frame_digest import FrameDigest
from mock import Mock, MagicMock, patch
from nose_parameterized import parameterized
import inspect
import unittest

class TestFrameDigest(unittest.TestCase):

    @parameterized.expand([('module1',), ('module2',)])
    def test_init_gets_module_name_from_frame(self, expected_module_name):
        frame_mock = Mock()
        frame_mock.f_globals = MagicMock()
        frame_mock.f_globals.__getitem__.return_value = expected_module_name
        
        frame_digest = FrameDigest(frame_mock)
        actual_module_name = frame_digest.module_name

        self.assertEqual(actual_module_name, expected_module_name)

    @parameterized.expand([('func1',), ('func2',)])
    def test_init_gets_function_name_from_frame(self, expected_function_name):
        frame_mock = Mock()
        frame_mock.f_code.co_name = expected_function_name
        
        frame_digest = FrameDigest(frame_mock)
        actual_function_name = frame_digest.function_name

        self.assertEqual(actual_function_name, expected_function_name)

    @patch('os.path.abspath')
    def test_file_name_returns_full_path_to_file(self, abspath_mock):
        abspath_mock.return_value = 'absolute/path/to/file'
        frame_mock = Mock()
        frame_mock.f_code.co_filename = 'path/to/file'

        frame_digest = FrameDigest(frame_mock)
        actual_filename = frame_digest.file_name

        abspath_mock.assert_called_once_with('path/to/file')
        self.assertEqual(actual_filename, 'absolute/path/to/file')

    @parameterized.expand([(1,), (10,)])
    def test_line_number_returns_source_code_line_number(self, expected_lineno):
        frame_mock = Mock()
        frame_mock.f_lineno = expected_lineno 

        frame_digest = FrameDigest(frame_mock)
        actual_lineno = frame_digest.line_number

        self.assertEqual(actual_lineno, expected_lineno)

    def test_works_on_a_real_frame_object(self):
        frame = inspect.currentframe()
        frame_digest = FrameDigest(frame)
        actual_module_name = frame_digest.module_name
        actual_function_name = frame_digest.function_name
        actual_file_name = frame_digest.file_name        
        actual_lineno = frame_digest.line_number        
        self.assertEqual(actual_module_name, 'test_frame_digest')
        self.assertEqual(actual_function_name, 'test_works_on_a_real_frame_object')
        assert 'test_frame_digest.py' in actual_file_name
        assert actual_lineno

if __name__ == '__main__':
    unittest.main()
