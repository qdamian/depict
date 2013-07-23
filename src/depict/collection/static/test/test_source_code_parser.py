from StringIO import StringIO
from depict.collection.static.source_code_parser import SourceCodeParser
from mock import Mock, call, ANY
import unittest

class TestSourceCodeParser(unittest.TestCase):
    '''Only testing some basic cases in the assumption that AST does all
       the hard work well'''

    def test_no_notification(self):
        src_file = StringIO('')
        observer = Mock()
        source_code_parser = SourceCodeParser()
        source_code_parser.register(observer)

        source_code_parser.parse('', src_file)
        
        self.assertEquals(observer.on_class.call_count, 0)

    def test_notifies_one_class(self):
        src_file = StringIO(
                            'class MyClass():\n'
                            '    """ Some fake\n'
                            '        class"""\n'
                            '    pass')
        observer = Mock()
        source_code_parser = SourceCodeParser()
        source_code_parser.register(observer)
        
        source_code_parser.parse('', src_file)
        
        observer.on_class.assert_called_once_with('MyClass', ANY)

    def test_notifies_two_classes(self):
        src_file = StringIO('class Class1():\n'
                            '    pass\n'
                            'class Class2():\n'
                            '    pass')
        observer = Mock()
        source_code_parser = SourceCodeParser()
        source_code_parser.register(observer)
        
        source_code_parser.parse('', src_file)
        
        calls = [call('Class1', ANY), call('Class2', ANY)]
        observer.on_class.assert_has_calls(calls)

    def test_notifies_nestedClass_definitions(self):
        src_file = StringIO('class Class1():\n'
                            '    pass\n'
                            '    class Class2():\n'
                            '        pass')
        observer = Mock()
        source_code_parser = SourceCodeParser()
        source_code_parser.register(observer)
        
        source_code_parser.parse('', src_file)
        
        calls = [call('Class1', ANY), call('Class2', ANY)]
        observer.on_class.assert_has_calls(calls)

    def test_notifies_classes_with_unique_id(self):
        src_file = StringIO('class Class1():\n'
                            '    pass\n'
                            'class Class2():\n'
                            '    pass\n')
        observer = Mock()
        source_code_parser = SourceCodeParser()
        source_code_parser.register(observer)
        
        source_code_parser.parse('fake_file_name', src_file)
        
        (args1, _) = observer.on_class.call_args_list[0]
        (_, id1) = args1
        (args2, _) = observer.on_class.call_args_list[1]
        (_, id2) = args2
        self.assertEquals(id1, 'fake_file_name:1')
        self.assertEquals(id2, 'fake_file_name:3')

    def test_notifies_one_function(self):
        src_file = StringIO('def my_function():\n'
                            '    pass')
        observer = Mock()
        source_code_parser = SourceCodeParser()
        source_code_parser.register(observer)
        
        source_code_parser.parse('fake_file_name', src_file)
        
        observer.on_function.assert_called_once_with('my_function',
                                                     'fake_file_name:1',
                                                     None)

    def test_notifies_one_method(self):
        src_file = StringIO('class some_class:\n'
                            '    def some_method(self):\n'
                            '        pass')
        observer = Mock()
        source_code_parser = SourceCodeParser()
        source_code_parser.register(observer)
        
        source_code_parser.parse('fake_file_name', src_file)
        
        observer.on_function.assert_called_once_with('some_method',
                                                     'fake_file_name:2',
                                                     'fake_file_name:1')

    def test_notifies_one_function_and_one_method(self):
        src_file = StringIO('class some_class:\n'
                            '    def some_method(self):\n'
                            '        pass\n'
                            'def some_function():\n'
                            '    pass')
        observer = Mock()
        source_code_parser = SourceCodeParser()
        source_code_parser.register(observer)
        
        source_code_parser.parse('fake_file_name', src_file)
        
        calls = [call('some_method', 'fake_file_name:2', 'fake_file_name:1'),
                 call('some_function', 'fake_file_name:4', None)]
        observer.on_function.assert_has_calls(calls)        

    def test_ignores_error_if_observer_does_not_expect_notification(self):
        src_file = StringIO(
                            'class MyClass():\n'
                            '    """ Some fake\n'
                            '        class"""\n'
                            '    pass\n'
                            'def my_function():\n'
                            '    pass')
        observer = Mock()
        observer.on_class.side_effect = AttributeError
        observer.on_function.side_effect = AttributeError
        source_code_parser = SourceCodeParser()
        source_code_parser.register(observer)
        
        source_code_parser.parse('', src_file)
