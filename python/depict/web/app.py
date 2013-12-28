# region GPLv3 notice
# Copyright 2013 Damian Quiroga
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
# endregion

import logging

import os
import bottle


APP = bottle.Bottle()
root = os.path.join(os.path.dirname(__file__), "..", "..", "..",
                    "html5")

@APP.route('/')
def serve_index():
    return bottle.static_file("index.html", root=root)


@APP.route('/<filepath:path>')
def serve_static(filepath):
    return bottle.static_file(filepath, root=root)
