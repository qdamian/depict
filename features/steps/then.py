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

from nose.tools import *
import re

@then(u'I see basic usage information')
def step_impl(context):
    assert_in('usage', context.stdout)

@then(u'I see a link to the user guide')
def step_impl(context):
    assert_in('https://github.com/qdamian/depict/wiki/User-guide', context.stdout)

@then(u'I see a copyright notice')
def step_impl(context):
    assert_in('GPL', context.stdout)

@then(u'I see trace listed')
def step_impl(context):
    assert_in('depict.txt.trace', context.stdout)

@then(u'I see sequence_diagram listed')
def step_impl(context):
    assert_in('depict.html5.sequence_diagram', context.stdout)

@then(u'I see movie listed')
def step_impl(context):
    assert_in('depict.html5.movie', context.stdout)

@then(u'it executes successfully')
def step_impl(context):
    assert_equal(context.exit_code, 0)

@then(u'I see the function calls printed')
def step_impl(context):
    assert_in('say_hi', context.stdout)
    assert_in('elapsed', context.stdout)

@then(u'I see the class or module each called function belongs to')
def step_impl(context):
    assert_in('main.say_hi', context.stdout)
    assert_in('Stopwatch.elapsed', context.stdout)

@then(u'the execution with depict is no more than {diff}% slower')
def step_impl(context, diff):
    without_depict = context.sample_mean_time
    with_depict = context.depict_sample_mean_time
    actual_diff = ((with_depict - without_depict) / without_depict) * 100
    expected_diff = long(diff)
    assert_less_equal(actual_diff, expected_diff)

@then(u'I see the module name for each function call')
def step_impl(context):
    assert_in('main', context.stdout)
    assert_in('util.stopwatch', context.stdout)
    assert_in('util.stopwatch', context.stdout)

@then(u'I see two function calls')
def step_impl(context):
    assert_equal(len(re.findall('say_hi', context.stdout)), 2)
