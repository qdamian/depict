from depict.processing.static_data_collector import StaticDataCollector
from mock import Mock, patch, ANY
import unittest

@patch('depict.processing.static_data_collector.open', create=True)
class TestStaticDataCollector(unittest.TestCase):

    def test_include_stores_collector(self, open_mock):
        fake_collector = Mock()
        fake_collector_class = Mock(return_value=fake_collector)
        static_data_collector = StaticDataCollector()
        static_data_collector.include(fake_collector_class)
        static_data_collector.process('fake_file_name')
        fake_collector.process.assert_called_once_with('fake_file_name', ANY)