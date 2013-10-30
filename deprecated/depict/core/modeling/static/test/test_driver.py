#region GPLv3 notice
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
#endregion

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
        self.static_driver = StaticDriver(self.file_set, self.model)

    def tearDown(self):
        self.patcher.stop()

    def test_it_models_data_from_each_file(self):
        # Arrange
        self.file_set.__iter__.return_value = ['a.py', 'path/to/b.py']

        # Act
        self.static_driver.run()

        # Assert
        self.orchestrator_mock.process.assert_called_once_with(['a.py', 'path/to/b.py'])
