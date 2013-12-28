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

from mock import Mock
from depict.web.socket import Socket


class TestSocket(object):

    def setUp(self):
        self.socket = Socket(None, None)
        Socket.USER = None

    def test_tells_the_user_when_the_socket_is_opened(self):
        # Arrange
        Socket.USER = Mock()

        # Act
        self.socket.opened()

        # Assert
        Socket.USER.on_web_socket_opened.assert_called_once_with(self.socket)

    def does_not_raise_exception_when_socket_is_opened_with_user_unknown(self):
        # Act
        self.socket.opened()

        # Assert that no exception is raised

    def test_sends_message(self):
        # Arrange
        self.socket.send = Mock()

        # Act
        self.socket.send_message('hi')

        # Assert
        self.socket.send.assert_called_once_with('hi')

    def test_tells_the_user_when_the_socket_is_closed(self):
        # Arrange
        Socket.USER = Mock()

        # Act
        self.socket.closed(code=123, reason="everything has an end")

        # Assert
        Socket.USER.on_web_socket_closed.assert_called_once_with()

    def does_not_raise_exception_when_socket_is_closed_with_user_unknown(self):
        # Arrange
        self.socket.opened()

        # Act
        self.socket.closed()

        # Assert that no exception is raised
