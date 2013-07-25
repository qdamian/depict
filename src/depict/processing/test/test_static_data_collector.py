# Copyright 2013 Damian Quiroga
#
# This file is part of Depict.
#
# Depict is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Depict is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Depict.  If not, see <http://www.gnu.org/licenses/>.

from depict.processing.static_data_collector import StaticDataCollector
from mock import Mock, patch, ANY
import unittest

@patch('depict.processing.static_data_collector.open', create=True)
class TestStaticDataCollector(unittest.TestCase):

    def test_include_stores_collector(self, open_mock):
        with patch('depict.processing.static_data_collector.GlobalSourceCodeParser'):
            fake_collector = Mock()
            fake_collector_class = Mock(return_value=fake_collector)
            static_data_collector = StaticDataCollector()
            static_data_collector.include(fake_collector_class)
            static_data_collector.process('fake_file_name')
            fake_collector_class.assert_called_once_with()