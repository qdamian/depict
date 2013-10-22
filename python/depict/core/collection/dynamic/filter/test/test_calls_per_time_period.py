#region GPLv3 notice
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
#endregion

from mock import Mock
from nose.tools import *

from depict.test.object_factory import fake
from depict.core.collection.dynamic.filter.calls_per_time_period import CallsPerTimePeriod


class TestCallsPerTimePeriod():
    def setUp(self):
        self.handler = Mock()
        self.frame_digest = fake('FrameDigest')

    def test_it_proxies_a_single_function_call(self):
        # Arrange
        call_filter = CallsPerTimePeriod(1, 1, self.handler)

        # Act
        call_filter.on_call(self.frame_digest)

        # Assert
        self.handler.on_call.assert_called_once_with(self.frame_digest)

    def test_it_discards_a_function_call_if_it_exceeds_the_call_rate(self):
        # Arrange
        call_filter = CallsPerTimePeriod(1, 1, self.handler)

        # Act
        call_filter.on_call(self.frame_digest)
        call_filter.on_call(self.frame_digest)

        # Assert
        self.handler.on_call.assert_called_once_with(self.frame_digest)

    def test_it_proxies_calls_after_the_call_period_elapses(self):
        # Arrange
        call_filter = CallsPerTimePeriod(1, 1, self.handler)

        # Act
        call_filter.on_call(self.frame_digest)
        call_filter._flush()
        call_filter.on_call(self.frame_digest)

        # Assert
        assert_equal(self.handler.on_call.call_count, 2)

    def test_it_proxies_calls_to_a_function_if_within_the_call_rate(self):
        # Arrange
        call_filter = CallsPerTimePeriod(3, 1, self.handler)

        # Act
        for _ in range(4):
            call_filter.on_call(self.frame_digest)

        # Assert
        assert_equal(self.handler.on_call.call_count, 3)

    def test_on_call_the_return_value_tells_if_the_call_was_proxied(self):
        # Arrange
        call_filter = CallsPerTimePeriod(1, 1, self.handler)

        # Act
        proxied_result = call_filter.on_call(self.frame_digest)
        discarded_result = call_filter.on_call(self.frame_digest)

        # Assert
        assert_true(proxied_result)
        assert_false(discarded_result)

    def test_other_function_calls_are_proxied_if_one_exceeds_the_call_rate(
            self):
        # Arrange
        call_filter = CallsPerTimePeriod(1, 1, self.handler)
        another_frame_digest = fake('FrameDigest')
        another_frame_digest.function_name = 'another_function'

        # Act
        proxied_result = call_filter.on_call(self.frame_digest)
        another_result = call_filter.on_call(another_frame_digest)
        discarded_result = call_filter.on_call(self.frame_digest)

        # Assert
        assert_true(proxied_result)
        assert_true(another_result)
        assert_false(discarded_result)
