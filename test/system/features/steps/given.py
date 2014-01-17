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

from behaving.web.steps import *


@given(u'my program has modules aa_mod, ab_mod, ba_mod, bb_mod')
@given(u'my program has functions aa_func, ab_func, ba_func, bb_func')
@given(u'my program spawns four threads')
def step_impl(context):
    context.program_path = os.path.abspath(
        os.path.join('test', 'system', 'data', 'one', 'main.py'))
