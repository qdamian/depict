#region GPLv3 notice
# Copyright 2014 Damian Quiroga
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

from nose.tools import *


def get_options(context):
    browser = context.browser
    control = browser.find_by_css("#search + .selectize-control")
    options = [x.text for x in control.find_by_css(".selectize-dropdown-content").find_by_css("div")]
    return options

@then(u'I see no options')
def step_impl(context):
    options = get_options(context)
    assert_equal(options, [])

@then(u'I see options {options}')
def step_impl(context, options):
    expected_options = options.split(", ")
    actual_options = get_options(context)
    assert_equal(set(actual_options), set(expected_options))

@then(u'I see ab among the available options')
def step_imp(context):
    expected_options = set(['ab'])
    actual_options = set(get_options(context))
    assert_true(expected_options.issubset(actual_options))
