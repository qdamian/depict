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
from utils import call
import re

@when(u'I run depict with incorrect options')
def step_impl(context):
    proc = call('python -m depict')
    context.stdout = proc.stdout.read()

@when(u'I run depict asking for the list of available representations')
def step_impl(context):
    proc = call('python -m depict --list')
    context.stdout = proc.stdout.read()

@when(u'I run the sample program')
def step_impl(context):
    proc = call('python ' + context.sample_program_main)
    context.exit_code = proc.wait()

@when(u'I run depict with the trace representation')
def step_impl(context):
    proc = call('python -m depict.txt.trace ' + context.sample_program_main)
    context.stdout = proc.stdout.read()

@when(u'I time the sample program')
def step_impl(context):
    cmd = 'python ' + context.sample_program_main
    context.sample_mean_time = time_sample_program(cmd)

@when(u'I time depict with the trace representation on the sample program')
def step_impl(context):
    cmd = 'python -m depict.txt.trace ' + context.sample_program_main
    context.depict_sample_mean_time = time_sample_program(cmd)

def time_sample_program(cmd):
    time = []
    for _ in range(3):
        proc = call(cmd)
        stdout = proc.stdout.read()
        time.append(float(re.findall('Elapsed time: (.*) msec', stdout)[0]))
    return sum(time) / len(time)
