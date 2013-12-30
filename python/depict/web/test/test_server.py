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

from random import random
import threading
from time import sleep
from mock import *
from nose.tools import *
from ws4py.client.threadedclient import WebSocketClient
from ws4py.websocket import EchoWebSocket
from webtest import TestApp
from depict.web.app import APP as WebApp
from depict.web.server import Server as WebServer


def ws_user_mock(server):
    server.wait_for_web_socket_opened()


class TestWebSocket(object):

    def __init__(self):
        self.web_server = None
        self.ws_client = None

    def setUp(self):
        WebServer.HTTP_PORT = int(random() * 1000) + 1024
        WebServer.WS_PORT = WebServer.HTTP_PORT + 1
        WebServer.WS_CLASS = EchoWebSocket
        self.web_server = WebServer()
        self.web_server.start(quiet=True)
        self.ws_client = WebSocketClient('ws://localhost:%s' %
                                         WebServer.WS_PORT,
                                         protocols=['http-only', 'chat'])

    def tearDown(self):
        try:
            self.ws_client.close()
            self.web_server.stop()
        except:
            pass

    def test_web_socket_server_accepts_connections(self):
        self.ws_client.opened = Mock()

        self.ws_client.connect()
        sleep(0.01)

        self.ws_client.opened.assert_called_once_with()

    def test_wait_for_web_socket_connection(self):
        thread = threading.Thread(target=ws_user_mock, args=(self.web_server,))
        thread.start()
        thread.join(timeout=0.1)
        assert_true(thread.isAlive())
        self.web_server.on_web_socket_opened(self)
        thread.join()
        assert_false(thread.isAlive())

    def test_wait_for_web_socket_again_after_closed(self):
        self.web_server.on_web_socket_opened(self)
        self.web_server.on_web_socket_closed()
        thread = threading.Thread(target=ws_user_mock, args=(self.web_server,))
        thread.start()
        thread.join(timeout=0.1)
        assert_true(thread.isAlive())
        self.web_server.on_web_socket_opened(self)
        thread.join()
        assert_false(thread.isAlive())

    def test_send_message_sends_it_using_the_web_socket(self):
        socket = Mock()
        self.web_server.on_web_socket_opened(socket)
        self.web_server.send_message('hi')
        socket.send.assert_called_once_with('hi')
