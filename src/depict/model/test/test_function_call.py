from depict.model.function_call import FunctionCall
from depict.model.function import Function
from depict.model.function_repo import GlobalFunctionRepo
import unittest

class TestFunctionCall(unittest.TestCase):
    def test_creation(self):
        FunctionCall('fake_function_id')
        
    def test_function_property(self):
        fake_function_id = 'fake_function_id'
        expected_function = Function('function_name', fake_function_id)
        GlobalFunctionRepo.add(expected_function)
        function_call = FunctionCall(fake_function_id)
        actual_function = function_call.function
        self.assertEqual(actual_function, expected_function)
        
    