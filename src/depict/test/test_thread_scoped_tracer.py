import unittest
from mock import Mock, call, ANY
from depict.thread_scoped_tracer import ThreadScopedTracer

def test_function1():
    return 1

def test_function2(arg):
    return arg

class TestThreadScopedTracer(unittest.TestCase):

    def test_notifies_one_function_call(self):
        observer = Mock()
        thread_scoped_tracer = ThreadScopedTracer(observer)
        thread_scoped_tracer.start()
        test_function1()
        thread_scoped_tracer.stop()
        observer.on_call.assert_called_once_with('test_function1')

    def test_notifies_two_function_calls(self):
        observer = Mock()
        thread_scoped_tracer = ThreadScopedTracer(observer)
        thread_scoped_tracer.start()
        test_function1()
        test_function2(1)
        thread_scoped_tracer.stop()
        expected_calls = [call('test_function1'), call('test_function2')]
        self.assertEqual(observer.on_call.call_args_list, expected_calls)

    def test_notifies_return_from_function(self):
        observer = Mock()
        thread_scoped_tracer = ThreadScopedTracer(observer)
        thread_scoped_tracer.start()
        test_function1()
        test_function2(1)
        thread_scoped_tracer.stop()
        expected_calls = [call('test_function1'), call('test_function2')]
        self.assertEqual(observer.on_call.call_args_list, expected_calls)

    def test_does_not_notify_after_stop(self):
        observer = Mock()
        thread_scoped_tracer = ThreadScopedTracer(observer)
        thread_scoped_tracer.start()
        test_function1()
        thread_scoped_tracer.stop()
        test_function2(1)
        observer.on_return.assert_called_once_with('test_function1')

if __name__ == '__main__':
    unittest.main()

if __name__ == '__main__':
    unittest.main()
