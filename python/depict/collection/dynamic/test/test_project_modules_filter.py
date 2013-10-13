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

from mock import Mock, MagicMock
from nose.tools import assert_equal
from depict.collection.dynamic.project_modules_filter import ProjectModulesFilter


class TestProjectModulesFilter():
    def test_it_proxies_function_calls_from_project_modules(self):
        observer = Mock()
        base_path = '/path/to/base'
        modules_filter = ProjectModulesFilter(base_path, observer)
        frame_digest = MagicMock()
        frame_digest.file_name = '/path/to/base/and/some/module.py'
        print 'a'
        print frame_digest.file_name
        print 'b'
        modules_filter.on_call(frame_digest)
        observer.on_call.assert_called_once_with(frame_digest)

    def test_is_filters_out_functions_calls_from_external_modules(self):
        observer = Mock()
        base_path = '/path/to/base'
        modules_filter = ProjectModulesFilter(base_path, observer)
        frame_digest = MagicMock()
        frame_digest.file_name = '/path/to/site-packages/and/external/module.py'
        modules_filter.on_call(frame_digest)
        assert_equal(observer.on_call.call_count, 0)