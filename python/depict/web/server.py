# region GPLv3 notice
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
# endregion

from depict.web.http_server_controller import HTTPServerController
from depict.web.web_socket_controller import WebSocketController


class Server(object):
    def __init__(self):
        self.web_server = HTTPServerController()
        self.web_socket = WebSocketController()

    def start(self, quiet=False):
        self.web_server.start()
        self.web_socket.start(self.web_server.http_port + 1)

    def stop(self):
        self.web_socket.stop()
        self.web_server.stop()

    def send_message(self, msg):
        self.web_socket.send_async(msg)

    @property
    def http_port(self):
        return self.web_server.http_port
