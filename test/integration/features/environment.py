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

from __future__ import absolute_import

from behaving import environment as behaving_env
from depict.data.sender import Sender as DataSender
from functools import wraps

def print_exceptions(f):
   @wraps(f)
   def wrapper(*args, **kwds):
       try:
           return f(*args, **kwds)
       except Exception as ex:
           print ex
           raise
   return wrapper

@print_exceptions
def before_all(context):
    behaving_env.before_all(context)
    context.data_sender = DataSender()
    context.data_sender.start()

@print_exceptions
def after_all(context):
    behaving_env.after_all(context)
    context.data_sender.stop()

@print_exceptions
def before_feature(context, feature):
    behaving_env.before_feature(context, feature)

@print_exceptions
def after_feature(context, feature):
    behaving_env.after_feature(context, feature)

@print_exceptions
def before_scenario(context, scenario):
    behaving_env.before_scenario(context, scenario)


@print_exceptions
def after_scenario(context, scenario):
    behaving_env.after_scenario(context, scenario)
