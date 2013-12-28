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
from ws4py.websocket import WebSocket



class Socket(WebSocket):
    # Using a class attribute due to lack of control over the instantiation
    USER = None

    def opened(self):
        logging.getLogger(__name__).debug('Web socket opened')
        if Socket.USER:
            Socket.USER.on_web_socket_opened(self)

    def send_message(self, msg):
        self.send(msg)

    def closed(self, code, reason=None):
        logging.getLogger(__name__).debug('Web socket closed (%s): %s' %
                                          (code, reason))
        if Socket.USER:
            Socket.USER.on_web_socket_closed()
