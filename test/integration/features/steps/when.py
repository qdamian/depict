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


@when(u'I open the app')
def step_impl(context):
    context.execute_steps(u'When I visit "http://localhost:8080"')


@when(u'I search {fill_text}')
def step_impl(context, fill_text):
    fill_search_with(context.browser, '\b%s' % fill_text)


@when(u'I hit Enter')
def step_impl(context):
    fill_search_with(context.browser, '\n')


def fill_search_with(browser, text):
    browser.find_by_css(".selectize-input").click()
    control = browser.find_by_css("#search + .selectize-control")[0]
    input_box = control.find_by_css("input")[0]
    input_box.value = text
