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

from depict.txt.trace.__main__ import main
from mock import patch, mock_open, Mock
from nose.tools import *
import depict
import os

@patch('sys.stderr', autospec=True)
@patch('argparse.ArgumentParser.exit', autospec=True)
@patch('depict.txt.trace.__main__.ProgramEnvEmulator', autospec=True)
@patch('depict.txt.trace.__main__.TraceRepr')
class TestMain():

    def test_returns_usage_when_no_options_are_passed(self, _1, _2, _3, _4):
        msg = main(['fake call to module'])
        assert_in('usage', msg)

    def test_returns_usage_when_user_asks_help(self, _1, _2, _3, _4):
        msg = main(['fake call to module', '--help'])
        assert_in('usage', msg)

    def test_runs_program_when_passed_as_positional_argument(self, _1, prog_env_emu_class_mock, _3, _4):
        prog_env_emu_mock = Mock()
        prog_env_emu_mock.code = 'raise TEST_EXCEPTION()'
        prog_env_emu_mock.globals = { 'TEST_EXCEPTION': ZeroDivisionError }
        prog_env_emu_class_mock.return_value = prog_env_emu_mock
        assert_raises(ZeroDivisionError, main, ['fake call to module', 'my_program.py'])

    def test_can_be_called_with_any_options_that_are_passed_to_the_called_program(self, _1, prog_env_emu_class_mock, _3, _4):
        prog_env_emu_mock = Mock()
        prog_env_emu_mock.code = 'pass'
        prog_env_emu_mock.globals = {}
        prog_env_emu_class_mock.return_value = prog_env_emu_mock
        main(['fake call to module', 'my_program.py', '--program-option1', '--program-option2'])
