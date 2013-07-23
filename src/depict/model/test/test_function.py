from depict.model.function import Function
import unittest

class TestFunction(unittest.TestCase):
    def test_creation(self):
        Function('fake_function_name', 'fake_function_id')
        
    def test_equal_comparison(self):
        function1 = Function('dummy_name1', 'fake_id1')
        function2 = Function('dummy_name2', 'fake_id1')
        self.assertEqual(function1, function2)