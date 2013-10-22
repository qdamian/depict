#region GPLv3 notice
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
#endregion

import threading
import bottle


class WebServer():
    def __init__(self):
        self.data = ''
        bottle.get('/entities', callback=self.get_entities)
        self.server_thread = None

    def start(self):
        self.server_thread = threading.Thread(target=bottle.run,
                                              kwargs={'host':'localhost',
                                                      'port':8080})
        self.server_thread.setDaemon(True)
        self.server_thread.start()

    def wait(self):
        self.server_thread.join()

    def handle(self, json_entity):
        self.data += json_entity

    def get_entities(self):
        response = self.data[:]
        self.data = ''
        return response
