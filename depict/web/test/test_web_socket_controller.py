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
from nose.tools import *

from depict.web.web_socket_controller import WebSocketController
from mock import ANY, patch, Mock


@patch('depict.web.web_socket_controller.WebSocketWSGIApplication')
@patch('depict.web.web_socket_controller.make_server')
class TestWebSocketControl(object):

    def test_start_creates_a_web_socket_wsgi_app(self, make_server, wsgi_app):
        # Given
        controller = WebSocketController()
        ws_class = WebSocketController.WS_CLASS

        # When
        controller.start(8080)

        # Then
        wsgi_app.assert_called_once_with(handler_cls=ws_class)

    def test_start_makes_the_ws_server(self, make_server, wsgi_app):
        # Given
        controller = WebSocketController()

        # When
        controller.start(999)

        # Then
        make_server.assert_called_once_with(host='localhost',
                                            port=999,
                                            server_class=ANY,
                                            handler_class=ANY,
                                            app=wsgi_app.return_value)

    def test_start_initialized_the_ws_manager(self, make_server, wsgi_app):
        # Given
        controller = WebSocketController()

        # When
        controller.start(8080)

        # Then
        ws_server = make_server.return_value
        ws_server.initialize_websockets_manager.assert_called_once_with()

    def test_start_listens_for_websocket_connections(self, make_server,
                                                     wsgi_app):
        # Given
        server_forever_called = threading.Event()
        ws_server = make_server.return_value
        ws_server.serve_forever.side_effect = server_forever_called.set
        controller = WebSocketController()

        # When
        controller.start(8080)

        # Then
        assert_true(server_forever_called.wait(1))

    def test_send_async_sends_message_after_the_web_socket_is_opened(self,
                                                                     make_server,
                                                                     wsgi_app):
        # Given
        controller = WebSocketController()
        ws = Mock()
        ws_send_called = threading.Event()

        ws.send.side_effect = lambda msg: ws_send_called.set()

        # When
        controller.start(8080)
        controller.send_async('hi')

        # Then
        assert_false(ws_send_called.wait(0.1))

        # When
        controller.on_web_socket_opened(ws)

        # Then
        assert_true(ws_send_called.wait(1))
        assert_equal(ws.send.call_args[0][0], 'hi')


    def test_stop_shuts_down_the_ws_server(self, make_server, wsgi_app):
        # Given
        controller = WebSocketController()
        controller.start(8080)

        # When
        controller.stop()

        # Then
        make_server.return_value.shutdown.assert_called_once_with()


    def test_stop_closes_the_websocket(self, make_server, wsgi_app):
        # Given
        controller = WebSocketController()
        controller.start(8080)
        ws = Mock()

        # When
        controller.on_web_socket_opened(ws)
        controller.stop()

        # Then
        ws.close.assert_called_once_with()
