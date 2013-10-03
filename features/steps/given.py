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

from nose.tools import assert_true, assert_false
from utils import call
import subprocess
import shutil
import os

@given(u'I dumped the sample program provided by depict')
def step_impl(context):
    # Arrange
    context.sample_program_dir = 'sample'
    context.sample_program_main = os.path.join(context.sample_program_dir, 'main.py')
    shutil.rmtree(context.sample_program_dir, ignore_errors=True)
    assert_false(os.path.isdir(context.sample_program_dir))
    cmd_line = 'python -m depict --sample ' + context.sample_program_dir

    # Act
    proc = call(cmd_line)
    proc.wait()

    # Assert
    assert_true(os.path.isdir(context.sample_program_dir))
