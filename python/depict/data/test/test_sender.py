#region GPLv3 notice
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
#endregion

from mock import patch
from depict.data.sender import Sender


@patch('depict.data.sender.WebServer')
class TestSender(object):

    def test_it_starts_the_web_server(self, web_server):
        Sender().start()
        web_server.return_value.start.assert_called_once_with()

    def test_sends_data_to_web_server(self, web_server):
        sender = Sender()
        sender.send_message('hi')
        web_server.return_value.send_message.assert_called_once_with('hi')

    def test_it_stops_the_web_server(self, web_server):
        sender = Sender()
        sender.stop()
        web_server.return_value.stop.assert_called_once_with()
