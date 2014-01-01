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

import threading

from wsgiref.simple_server import make_server
import bottle
from ws4py.server.wsgirefserver import WSGIServer, WebSocketWSGIRequestHandler
from ws4py.server.wsgiutils import WebSocketWSGIApplication
from depict.web.app import APP
from depict.web.socket import Socket as WebSocket

class HTTPServer(bottle.ServerAdapter):

    def run(self, handler):
        self.server = make_server(
            self.host, self.port, handler, **self.options)
        self.server.serve_forever()

class Server(object):
    """
    Serve static content and manage a web socket.
    """

    HTTP_PORT = 8080
    WS_PORT = 9876
    WS_CLASS = WebSocket

    def __init__(self):
        self.web_socket_opened = threading.Event()
        self.web_socket = None
        self.http_thread = None
        self.ws_thread = None

    def start(self, quiet=False):
        ws_app = WebSocketWSGIApplication(handler_cls=Server.WS_CLASS)
        self.ws_server = make_server(host='localhost',
                                     port=Server.WS_PORT,
                                     server_class=WSGIServer,
                                     handler_class=WebSocketWSGIRequestHandler,
                                     app=ws_app)
        self.ws_server.initialize_websockets_manager()
        self.http_thread = threading.Thread(target=self._start_http_server,
                                            args=(quiet,))
        self.http_thread.start()
        self.ws_thread = threading.Thread(target=self._start_ws_server)
        self.ws_thread.start()

    def _start_http_server(self, quiet):
        self.http_server = HTTPServer('localhost', Server.HTTP_PORT)
        APP.run(server=self.http_server, quiet=quiet)

    def _start_ws_server(self):
        self.WS_CLASS.USER = self
        self.ws_server.serve_forever()

    def stop(self):
        # if self.web_socket:
        #     self.web_socket.close_connection()
        self.http_server.server.shutdown()
        self.ws_server.shutdown()
        self.ws_thread.join()
        self.http_thread.join()

    def send_message(self, msg):
        self.web_socket.send(msg)

    def wait_for_web_socket_opened(self):
        self.web_socket_opened.wait()

    def on_web_socket_opened(self, web_socket):
        self.web_socket = web_socket
        self.web_socket_opened.set()

    def on_web_socket_closed(self):
        self.web_socket_opened.clear()
        self.web_socket = None
