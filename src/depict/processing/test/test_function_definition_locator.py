from depict.processing.function_definition_locator import FunctionDefinitionLocator
from depict.model.function_repo import FunctionRepo
from mock import Mock
from depict.model.function import Function
import unittest

class TestFunctionDefinitionLocator(unittest.TestCase):
    def test_creation(self):
        Functionrepo_ = FunctionRepo()
        code_parser_mock = Mock()
        class_def_locator = FunctionDefinitionLocator(code_parser_mock,
                                                   Functionrepo_)
        code_parser_mock.register.assert_called_once_with(class_def_locator)

    def test_adds_oneFunctionto_repo(self):
        function_repo_mock = Mock()
        code_parser_mock = Mock()
        class_def_locator = FunctionDefinitionLocator(code_parser_mock,
                                                   function_repo_mock)
        expected_function = Function('fakeFunctionname',
                                       'fakeFunctionid')
        code_parser_mock.parse.side_effect = (lambda a, b:
                                class_def_locator.on_function(expected_function.name,
                                                           expected_function.id_,
                                                           None))
        class_def_locator.process('fake_file_name', 'fake_code') 
        code_parser_mock.parse.assert_called_once_with('fake_file_name',
                                                       'fake_code')
        (args, _) = function_repo_mock.add.call_args
        actual_function = args[0]
        self.assertEqual(actual_function.name, expected_function.name)
        self.assertEqual(actual_function.id_, expected_function.id_)
