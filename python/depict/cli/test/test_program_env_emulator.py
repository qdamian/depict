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

from depict.cli.program_env_emulator import ProgramEnvEmulator
from nose.tools import *
from mock import mock_open, patch, Mock

@patch('__builtin__.open', new=mock_open(None, 'test_var = "test_value"'))
class TestdepictedProgEnvEmulator():

    def test_generates_global_variables_to_emulate_main_namespace(self):
        # Arrange
        argv = ['path/to/representation/__main__.py', 'expected_program_name.py', 'args']

        # Act
        program_env_emulator = ProgramEnvEmulator(argv)

        # Assert
        assert_equal(program_env_emulator.globals['__file__'], 'expected_program_name.py')
        assert_equal(program_env_emulator.globals['__name__'], '__main__')
        assert_equal(program_env_emulator.globals['__package__'], None)
        assert_equal(program_env_emulator.globals['__cached__'], None)

    def test_compiles_the_program(self):
        # Arrange
        argv = ['path/to/representation/__main__.py', 'expected_program_name.py', 'args']

        # Act
        program_env_emulator = ProgramEnvEmulator(argv)
        exec program_env_emulator.code

        # Assert
        assert_equal(test_var, 'test_value')
        assert_equal(program_env_emulator.code.co_filename, 'expected_program_name.py')