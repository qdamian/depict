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

import subprocess
import os

@when(u'I run depict with incorrect options')
def step_impl(context):
    proc = subprocess.Popen('python -m depict'.split(), stdout=subprocess.PIPE)
    context.stdout = proc.stdout.read()

@when(u'I run depict asking for the list of available representations')
def step_impl(context):
    proc = subprocess.Popen('python -m depict --list'.split(), stdout=subprocess.PIPE)
    context.stdout = proc.stdout.read()

@when(u'I run the sample program')
def step_impl(context):
    context.sample_program_dir = 'sample'
    sample_program_main = os.path.join(context.sample_program_dir, 'main.py')
    cmd_line = 'python ' + sample_program_main
    context.exit_code = subprocess.call(cmd_line.split())
