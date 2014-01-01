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

@given(u'my program has modules {modules}')
def step_impl(context, modules):
    for mod in modules.split(','):
        msg = '''
            {
                "id_":"../aa.py",
                "name":"%s",
                "parent":null,
                "dependencies":[],
                "branch_depth":0,
                "type":"Module",
                "children":[]
            }
        ''' % mod.strip()
        context.data_sender.send_message(msg)
