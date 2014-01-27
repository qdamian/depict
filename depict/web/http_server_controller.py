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

from __future__ import absolute_import

import threading
from wsgiref.simple_server import make_server
import socket
import bottle
from depict.web.app import APP


class HTTPAdapter(bottle.ServerAdapter):
    def run(self, handler):
        self.server = make_server(
            self.host, self.port, handler, **self.options)
        HTTPServerController.http_port_bound.set()
        self.server.serve_forever()


class HTTPServerController(object):
    http_port_bound = threading.Event()

    def __init__(self):
        self.http_port = 8090
        self.http_thread = None
        HTTPServerController.http_port_bound.clear()

    def start(self, quiet=False):
        self.http_thread = threading.Thread(target=self._start_http_server,
                                            args=(quiet,))
        self.http_thread.setDaemon(True)
        self.http_thread.start()
        if not HTTPServerController.http_port_bound.wait(1):
            raise Exception("Could not find a free port for the HTTP server")

    def _start_http_server(self, quiet):
        for _ in range(10):
            try:
                self.http_server = HTTPAdapter('localhost', self.http_port)
                APP.run(server=self.http_server, quiet=quiet)
                return
            except socket.error:
                self.http_port += 2

    def stop(self):
        if APP: APP.close()
        if self.http_server: self.http_server.server.shutdown()
        if self.http_thread: self.http_thread.join()
