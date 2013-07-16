import unittest
from mock import Mock, call, ANY
from depict.collection.dynamic.thread_scoped_tracer import ThreadScopedTracer

def function1():
    return 1

def function2(arg):
    return arg

class TestThreadScopedTracer(unittest.TestCase):

    def test_notifies_one_function_call(self):
        observer = Mock()
        thread_scoped_tracer = ThreadScopedTracer(observer)
        thread_scoped_tracer.start()
        function1()
        thread_scoped_tracer.stop()
        self.assertEqual(observer.on_call.call_count, 1)
        thread_digest = observer.on_call.call_args_list[0][0][0]
        actual_function_name = thread_digest.function_name
        self.assertEqual(actual_function_name, 'function1')

    def test_notifies_two_function_calls(self):
        observer = Mock()
        thread_scoped_tracer = ThreadScopedTracer(observer)
        thread_scoped_tracer.start()
        function1()
        function2(1)
        thread_scoped_tracer.stop()
        self.assertEqual(observer.on_call.call_count, 2)
        thread_digest1 = observer.on_call.call_args_list[0][0][0]
        actual_function_name1 = thread_digest1.function_name
        self.assertEqual(actual_function_name1, 'function1')
        thread_digest2 = observer.on_call.call_args_list[1][0][0]
        actual_function_name2 = thread_digest2.function_name
        self.assertEqual(actual_function_name2, 'function2')

    def test_notifies_return_from_function(self):
        observer = Mock()
        thread_scoped_tracer = ThreadScopedTracer(observer)
        thread_scoped_tracer.start()
        function1()
        thread_scoped_tracer.stop()
        self.assertEqual(observer.on_return.call_count, 1)
        thread_digest = observer.on_return.call_args_list[0][0][0]
        actual_function_name = thread_digest.function_name
        self.assertEqual(actual_function_name, 'function1')

    def test_does_not_notify_after_stop(self):
        observer = Mock()
        thread_scoped_tracer = ThreadScopedTracer(observer)
        thread_scoped_tracer.start()
        function1()
        thread_scoped_tracer.stop()
        function2(1)
        self.assertEqual(observer.on_call.call_count, 1)
        thread_digest = observer.on_call.call_args_list[0][0][0]
        actual_function_name = thread_digest.function_name
        self.assertEqual(actual_function_name, 'function1')

if __name__ == '__main__':
    unittest.main()
