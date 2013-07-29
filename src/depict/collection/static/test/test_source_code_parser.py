# Copyright 2013 Damian Quiroga
#
# This file is part of Depict.
#
# Depict is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Depict is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Depict.  If not, see <http://www.gnu.org/licenses/>.

from StringIO import StringIO
from depict.collection.static.source_code_parser import SourceCodeParser, \
                                                        PerformanceError
from mock import Mock, call, ANY, patch
import unittest

class TestSourceCodeParser(unittest.TestCase):
    '''Only testing some basic cases in the assumption that AST does all
       the hard work well'''

    def setUp(self):
        SourceCodeParser.parsed_files = []
        self.entity_id_mock = Mock()
        self.entity_id_mock.create.return_value = 'fake_id'
        self.entity_id_patcher = patch('depict.collection.static.source_code_parser.entity_id',
                                       self.entity_id_mock)
        self.entity_id_patcher.start()

    def tearDown(self):
        self.entity_id_patcher.stop()

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

        observer.on_class.assert_called_once_with(ANY, 'MyClass')

    def test_notifies_two_classes(self):
        src_file = StringIO('class Class1():\n'
                            '    pass\n'
                            'class Class2():\n'
                            '    pass')
        observer = Mock()
        source_code_parser = SourceCodeParser()
        source_code_parser.register(observer)

        source_code_parser.parse('', src_file)

        calls = [call(ANY, 'Class1'), call(ANY, 'Class2')]
        observer.on_class.assert_has_calls(calls)

    def test_notifies_nested_class_definition(self):
        src_file = StringIO('class Class1():\n'
                            '    pass\n'
                            '    class Class2():\n'
                            '        pass')
        observer = Mock()
        source_code_parser = SourceCodeParser()
        source_code_parser.register(observer)

        source_code_parser.parse('', src_file)

        calls = [call(ANY, 'Class1'), call(ANY, 'Class2')]
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
        (id1, _) = args1
        (args2, _) = observer.on_class.call_args_list[1]
        (id2, _) = args2
        self.assertEquals(id1, 'fake_file_name:1')
        self.assertEquals(id2, 'fake_file_name:3')

    def test_notifies_one_function(self):
        src_file = StringIO('def my_function():\n'
                            '    pass')
        observer = Mock()
        source_code_parser = SourceCodeParser()
        source_code_parser.register(observer)

        source_code_parser.parse('fake_file_name', src_file)

        observer.on_function.assert_called_once_with('fake_file_name:1',
                                                     'my_function',
                                                     None)

    def test_notifies_one_method(self):
        src_file = StringIO('class some_class:\n'
                            '    def some_method(self):\n'
                            '        pass')
        observer = Mock()
        source_code_parser = SourceCodeParser()
        source_code_parser.register(observer)

        source_code_parser.parse('fake_file_name', src_file)

        observer.on_function.assert_called_once_with('fake_file_name:2',
                                                     'some_method',
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

        calls = [call('fake_file_name:2', 'some_method', 'fake_file_name:1'),
                 call('fake_file_name:4', 'some_function', None)]
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

    def test_notifies_one_module(self):
        src_file = StringIO('import os\n'
                            'os.path.join("a", "b")')
        observer = Mock()
        source_code_parser = SourceCodeParser()
        source_code_parser.register(observer)

        self.entity_id_mock.create.return_value = 'to/fake_module.pyc'
        source_code_parser.parse('path/to/fake_module.pyc', src_file)

        observer.on_module.assert_called_once_with('to/fake_module.pyc',
                                                   'to.fake_module')

    def test_complains_if_a_file_is_parsed_more_than_once(self):
        src_file = StringIO('pass')
        source_code_parser = SourceCodeParser()
        source_code_parser.parse('fake_file_name.py', src_file)
        self.assertRaises(PerformanceError, source_code_parser.parse,
                          'fake_file_name.py', src_file)

