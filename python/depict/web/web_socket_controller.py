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

import Queue

import threading
from wsgiref.simple_server import make_server
from ws4py.server.wsgirefserver import WSGIServer, WebSocketWSGIRequestHandler
from ws4py.server.wsgiutils import WebSocketWSGIApplication
from depict.web.socket import Socket as WebSocket


class WebSocketController(object):
    WS_CLASS = WebSocket

    def __init__(self):
        self.web_socket_opened = threading.Event()
        self.web_socket = None
        self.ws_thread = None
        self.msg_queue = Queue.Queue()
        self.processing_thread = None

    def start(self, port, quiet=False):
        ws_app = WebSocketWSGIApplication(
                                     handler_cls=WebSocketController.WS_CLASS)
        self.ws_server = make_server(host='localhost',
                                     port=port,
                                     server_class=WSGIServer,
                                     handler_class=WebSocketWSGIRequestHandler,
                                     app=ws_app)
        self.ws_server.initialize_websockets_manager()
        self._start_ws_thread()
        self._start_msg_processing_thread()


    def _start_ws_thread(self):
        self.ws_thread = threading.Thread(target=self._start_ws_server)
        self.ws_thread.setDaemon(True)
        self.ws_thread.start()


    def _start_ws_server(self):
        self.WS_CLASS.USER = self
        self.ws_server.serve_forever()

    def stop(self):
        if self.web_socket: self.web_socket.close()
        if self.ws_server: self.ws_server.shutdown()
        if self.ws_thread: self.ws_thread.join()
        if self.processing_thread: self.processing_thread.join()
        self.web_socket_opened.clear()

    def send_async(self, msg):
        self.msg_queue.put(msg)

    def on_web_socket_opened(self, web_socket):
        self.web_socket = web_socket
        self.web_socket_opened.set()

    def on_web_socket_closed(self):
        self.web_socket_opened.clear()
        self.web_socket = None

    def _process_msg_queue(self):
        while True:
            msg = self.msg_queue.get()
            self._wait_for_web_socket_opened()
            self.web_socket.send(msg)

    def _wait_for_web_socket_opened(self):
        self.web_socket_opened.wait()


    def _start_msg_processing_thread(self):
        processing_thread = threading.Thread(target=self._process_msg_queue)
        processing_thread.setDaemon(True)
        processing_thread.start()

