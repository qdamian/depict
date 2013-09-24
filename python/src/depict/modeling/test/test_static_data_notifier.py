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
from depict.modeling.class_def_collector import ClassDefCollector
from depict.modeling.function_def_collector import FunctionDefCollector
from depict.modeling.module_def_collector import ModuleDefCollector
from depict.modeling.static_data_notifier import StaticDataNotifier
from mock import Mock, call, MagicMock, patch
import unittest
from depict.model.module import Module
from formic.formic import FileSet

class TestStaticDataNotifier(unittest.TestCase):
    def setUp(self):
        self.file_set_mock = MagicMock()
        self.file_set_mock.directory = '.'

    def test_init(self):
        dummy_file_list = ['a.py', 'path/to/b.py']
        dummy_observer = Mock()
        StaticDataNotifier(dummy_file_list, dummy_observer, Mock())

    def test_collects_data_from_each_file(self):
        file_set_mock = MagicMock()
        file_set_mock.__iter__.return_value = ['a.py', 'path/to/b.py']
        dummy_observer = Mock()
        def_collection_orchestrator_mock = Mock()
        static_data_notifier = StaticDataNotifier(file_set_mock, dummy_observer, def_collection_orchestrator_mock)
        static_data_notifier.run()
        def_collection_orchestrator_mock.process.assert_called_once_with(['a.py', 'path/to/b.py'])

    @patch('depict.modeling.static_data_notifier.global_module_repo')
    def test_notifies_collected_modules(self, module_repo_mock):
        fake_module = Module('fake_module_id', 'fake_function_name')
        module_repo_mock.get_all.return_value = [fake_module]
        fake_observer = Mock()
        static_data_notifier = StaticDataNotifier(self.file_set_mock, fake_observer, Mock())

        static_data_notifier.run()

        expected_calls = [call(fake_module)]
        fake_observer.on_module.assert_has_calls(expected_calls)

    @patch('depict.modeling.static_data_notifier.global_class_repo')
    def test_notifies_collected_classes(self, class_repo_mock):
        fake_class_1 = Class_('fake_class_id1', 'fake_class_name1')
        fake_class_2 = Class_('fake_class_id2', 'fake_class_name2')
        class_repo_mock.get_all.return_value = [fake_class_1, fake_class_2]
        fake_observer = Mock()
        static_data_notifier = StaticDataNotifier(self.file_set_mock, fake_observer, Mock())

        static_data_notifier.run()

        expected_calls = [call(fake_class_1), call(fake_class_2)]
        fake_observer.on_class.assert_has_calls(expected_calls)

    @patch('depict.modeling.static_data_notifier.global_function_repo')
    def test_notifies_collected_functions(self, function_repo_mock):
        fake_function = Function('fake_function_name', 'fake_function_id')
        fake_class = Class_('fake_class_id', 'fake_class_name')
        fake_method = Method('fake_method_id', 'fake_method_name', fake_class)
        function_repo_mock.get_all.return_value = [fake_function, fake_method]
        fake_observer = Mock()
        static_data_notifier = StaticDataNotifier(self.file_set_mock, fake_observer, Mock())

        static_data_notifier.run()

        expected_calls = [call(fake_function), call(fake_method)]
        fake_observer.on_function.assert_has_calls(expected_calls)

    def test_ignores_error_if_observer_does_not_expect_a_notification(self):
        function_repo_mock = Mock()
        fake_function = Function('fake_function_name', 'fake_function_id')
        function_repo_mock.get_all.return_value = [fake_function]
        fake_observer = Mock()
        fake_observer.on_function.side_effect = AttributeError
        static_data_notifier = StaticDataNotifier(self.file_set_mock, fake_observer, Mock())
        static_data_notifier.run()

    def test_ignores_error_if_observer_does_not_expect_a_notification(self):
        function_repo_mock = MagicMock()
        fake_observer = Mock()
        static_data_notifier = StaticDataNotifier(self.file_set_mock, fake_observer, Mock())
        static_data_notifier.run()
        fake_observer.on_collection_completed.assert_called_once_with()
