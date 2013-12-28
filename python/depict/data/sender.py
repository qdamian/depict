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

import logging
import threading
from depict.web.server import Server as WebServer

class Sender(object):

    def __init__(self):
        self.server = WebServer()

    def start(self):
        self.server.start()

    def send_message(self, data):
        thread = threading.Thread(target=self._do_send, args=(data,))
        thread.start()

    def _do_send(self, data):
        self.server.wait_for_web_socket_opened()
        self.server.send_message(data)

    def stop(self):
        self.server.stop()
