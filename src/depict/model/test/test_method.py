from depict.model.method import Method
import unittest

class TestMethod(unittest.TestCase):
    def test_creation(self):
        Method('fake_function_name',
                   'fake_function_id',
                   'fake_parent')
        
    def test_eq_comparison(self):
        method1 = Method('dummy_function_name1', 'fake_id1', 'dummy_parent1')
        method2 = Method('dummy_function_name2', 'fake_id1', 'dummy_parent2')
        self.assertEqual(method1, method2)
