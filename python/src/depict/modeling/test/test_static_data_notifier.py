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

from depict.model.class_ import Class_
from depict.model.function import Function
from depict.model.method import Method
from depict.modeling.class_definition_collector import \
    ClassDefinitionCollector
from depict.modeling.function_definition_collector import \
    FunctionDefinitionCollector
from depict.modeling.module_definition_collector import \
    ModuleDefinitionCollector
from depict.modeling.static_data_notifier import StaticDataNotifier
from mock import patch, Mock, call
import unittest
from depict.model.module import Module

@patch('depict.modeling.static_data_notifier.GlobalDefinitionCollectionOrchestrator')


class TestStaticDataNotifier(unittest.TestCase):

    def test_init(self, collection_orchestrator_mock):
        dummy_file_list = ['a.py', 'path/to/b.py']
        dummy_observer = Mock()
        StaticDataNotifier(dummy_file_list, dummy_observer)

    def test_collects_data_from_each_file(self, collection_orchestrator_mock):
        fake_file_list = ['a.py', 'path/to/b.py']
        dummy_observer = Mock()
        static_data_notifier = StaticDataNotifier(fake_file_list, dummy_observer)
        static_data_notifier.run()
        collection_orchestrator_mock.process.assert_called_once_with(['a.py', 'path/to/b.py'])

    def test_includes_module_definitions(self, collection_orchestrator_mock):
        static_data_notifier = StaticDataNotifier('dummy_file.py', Mock())
        static_data_notifier.run()
        collection_orchestrator_mock.include.assert_has_calls(call(ModuleDefinitionCollector))

    def test_includes_class_definitions(self, collection_orchestrator_mock):
        static_data_notifier = StaticDataNotifier('dummy_file.py', Mock())
        static_data_notifier.run()
        collection_orchestrator_mock.include.assert_has_calls(call(ClassDefinitionCollector))

    def test_includes_function_definitions(self, collection_orchestrator_mock):
        static_data_notifier = StaticDataNotifier('dummy_file.py', Mock())
        static_data_notifier.run()
        collection_orchestrator_mock.include.assert_has_calls(call(FunctionDefinitionCollector))

    def test_notifies_collected_modules(self, collection_orchestrator_mock):
        with patch('depict.modeling.static_data_notifier.GlobalModuleRepo') as module_repo_mock:
            fake_module = Module('fake_module_id', 'fake_function_name')
            module_repo_mock.get_all.return_value = [fake_module]
            fake_observer = Mock()
            static_data_notifier = StaticDataNotifier('dummy_file.py', fake_observer)
            static_data_notifier.run()
            expected_calls = [call(fake_module)]
            fake_observer.on_module.assert_has_calls(expected_calls)

    def test_notifies_collected_classes(self, collection_orchestrator_mock):
        with patch('depict.modeling.static_data_notifier.GlobalClassRepo') as class_repo_mock:
            fake_class_1 = Class_('fake_class_id1', 'fake_class_name1')
            fake_class_2 = Class_('fake_class_id2', 'fake_class_name2')
            class_repo_mock.get_all.return_value = [fake_class_1, fake_class_2]
            fake_observer = Mock()
            static_data_notifier = StaticDataNotifier('dummy_file.py', fake_observer)
            static_data_notifier.run()
            expected_calls = [call(fake_class_1), call(fake_class_2)]
            fake_observer.on_class.assert_has_calls(expected_calls)

    def test_notifies_collected_functions(self, collection_orchestrator_mock):
        with patch('depict.modeling.static_data_notifier.GlobalFunctionRepo') as function_repo_mock:
            fake_function = Function('fake_function_name', 'fake_function_id')
            fake_class = Class_('fake_class_id', 'fake_class_name')
            fake_method = Method('fake_method_id', 'fake_method_name', fake_class)
            function_repo_mock.get_all.return_value = [fake_function, fake_method]
            fake_observer = Mock()
            static_data_notifier = StaticDataNotifier('dummy_file.py', fake_observer)
            static_data_notifier.run()
            expected_calls = [call(fake_function), call(fake_method)]
            fake_observer.on_function.assert_has_calls(expected_calls)

    def test_ignores_error_if_observer_does_not_expect_a_notification(self, collection_orchestrator_mock):
        with patch('depict.modeling.static_data_notifier.GlobalFunctionRepo') as function_repo_mock:
            fake_function = Function('fake_function_name', 'fake_function_id')
            function_repo_mock.get_all.return_value = [fake_function]
            fake_observer = Mock()
            fake_observer.on_function.side_effect = AttributeError
            static_data_notifier = StaticDataNotifier('dummy_file_.py', fake_observer)
            static_data_notifier.run()
