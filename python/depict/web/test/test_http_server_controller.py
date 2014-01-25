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

import socket
from nose.tools import *
from depict.web.http_server_controller import HTTPServerController
from mock import patch


@patch('depict.web.http_server_controller.HTTPAdapter')
@patch('depict.web.http_server_controller.APP')
class TestHttpServerController(object):
    def test_start_binds_a_socket_using_an_even_port_number(self, app,
                                                             http_adapter):
        # Given
        controller = HTTPServerController()
        app.run.side_effect = controller.http_port_bound.set()

        # When
        controller.start()

        # Then
        assert_true(controller.http_port_bound.wait(1))
        bound_port = http_adapter.call_args[0][1]
        assert_equal(bound_port % 2, 0)
