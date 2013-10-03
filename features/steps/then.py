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

from nose.tools import assert_equal

@then(u'I see basic usage information')
def step_impl(context):
    assert 'usage' in context.stdout

@then(u'I see a link to the user guide')
def step_impl(context):
    assert 'https://github.com/qdamian/depict/wiki/User-guide' in context.stdout

@then(u'I see a copyright notice')
def step_impl(context):
    assert 'GPL' in context.stdout

@then(u'I see trace listed')
def step_impl(context):
    assert 'depict.txt.trace' in context.stdout

@then(u'I see sequence_diagram listed')
def step_impl(context):
    assert 'depict.html5.sequence_diagram' in context.stdout

@then(u'I see movie listed')
def step_impl(context):
    assert 'depict.html5.movie' in context.stdout

@then(u'it executes successfully')
def step_impl(context):
    assert_equal(context.exit_code, 0)

@then(u'I see the function calls printed')
def step_impl(context):
    assert 'main' in context.stdout
    assert 'say_hi' in context.stdout
    assert 'say_bye' in context.stdout
