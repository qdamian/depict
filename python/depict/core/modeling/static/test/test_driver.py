# Copyright 2013 Damian Quiroga
#
# This file is part of depict.
#
# depict is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# depict is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with depict.  If not, see <http://www.gnu.org/licenses/>.

from mock import Mock, call, patch

from depict.core.modeling.static.driver import Driver as StaticDriver
from depict.test.object_factory import fake, real, unique


class TestDriver():
    def setUp(self):
        self.patcher = patch('depict.core.modeling.static.driver.Orchestrator')
        self.orchestrator_mock = Mock()
        self.orchestrator_class = self.patcher.start()
        self.orchestrator_class.return_value = self.orchestrator_mock

        self.file_set = fake('FileSet')
        self.observer = Mock()
        self.model = fake('Model')
        self.static_driver = StaticDriver(self.file_set,
                                           self.observer,
                                           self.model)

    def tearDown(self):
        self.patcher.stop()

    def test_it_models_data_from_each_file(self):
        # Arrange
        self.file_set.__iter__.return_value = ['a.py', 'path/to/b.py']

        # Act
        self.static_driver.run()

        # Assert
        self.orchestrator_mock.process.assert_called_once_with(['a.py', 'path/to/b.py'])

    def test_it_notifies_modeled_modules(self):
        # Arrange
        module = real('Module')
        self.model.modules.get_all.return_value = [module]

        # Act
        self.static_driver.run()

        # Assert
        self.observer.on_module.assert_has_calls([call(module)])

    def test_it_notifies_modeled_classes(self):
        # Arrange
        class_1 = unique(real('Class_'))
        class_2 = unique(real('Class_'))
        self.model.classes.get_all.return_value = [class_1, class_2]

        # Act
        self.static_driver.run()

        # Assert
        expected_calls = [call(class_1), call(class_2)]
        self.observer.on_class.assert_has_calls(expected_calls)

    def test_it_notifies_modeled_functions(self):
        # Arrange
        function = fake('Function')
        method = fake('Method')
        self.model.functions.get_all.return_value = [function, method]

        # Act
        self.static_driver.run()

        # Assert
        expected_calls = [call(function), call(method)]
        self.observer.on_function.assert_has_calls(expected_calls)

    def test_ignores_error_if_observer_does_not_expect_a_notification(self):
        # Arrange
        fake_function = real('Function')
        self.model.functions.get_all.return_value = [fake_function]
        self.observer.on_function.side_effect = AttributeError

        # Act
        self.static_driver.run()

        # Assert that no exceptions are raised