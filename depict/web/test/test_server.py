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

from depict.web.server import Server
from mock import patch


class TestServer(object):

    @patch('depict.web.server.HTTPServerController')
    @patch('depict.web.server.WebSocketController')
    def test_the_http_server_and_web_socket_use_consecutive_ports(self,
                                web_socket_controller, http_server_controller):
        # Given
        server = Server()
        http_server_controller.return_value.http_port = 1000

        # When
        server.start()

        # Then
        http_server_controller.return_value.start.assert_called_once_with()
        web_socket_controller.return_value.start.assert_called_once_with(1001)
