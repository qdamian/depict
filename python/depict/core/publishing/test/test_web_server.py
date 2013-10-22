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

from nose.tools import *

from depict.core.publishing.web_server import WebServer

class TestWebServer():

    def test_it_returns_nothing_by_default(self):
        # Arrange nothing
        # Act
        assert_equal(WebServer().get_entities(), '')

    def test_it_returns_one_entity(self):
        # Arrange
        expected_data = '{ "id_":"test_entity" }'
        web_server = WebServer()
        web_server.handle(expected_data)

        # Act
        response = web_server.get_entities()

        # Assert
        assert_equal(response, expected_data)

    def test_it_returns_two_entities(self):
        # Arrange
        web_server = WebServer()
        data1 = '{ "id_":"aa" }'
        web_server.handle(data1)
        data2 = '{ "id_":"bb" }'
        web_server.handle(data2)

        # Act
        response = web_server.get_entities()

        # Assert
        assert_equal(response, data1 + data2)

    def test_it_returns_only_the_delta(self):
        # Arrange
        web_server = WebServer()
        data1 = '{ "id_":"aa" }'
        data2 = '{ "id_":"bb" }'

        # Act
        web_server.handle(data1)
        response1 = web_server.get_entities()
        web_server.handle(data2)
        response2 = web_server.get_entities()

        # Assert
        assert_equal(response1, data1)
        assert_equal(response2, data2)
