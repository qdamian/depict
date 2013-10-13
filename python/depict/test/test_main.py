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

from depict.__main__ import main
from mock import patch
from nose.tools import *
import depict
import os

@patch('sys.stderr', autospec=True)
@patch('argparse.ArgumentParser.exit', autospec=True)
class TestMain():

    def test_returns_usage_when_no_options_are_passed(self, _1, _2):
        msg = main(['dummy_prog', ''])
        assert_in('usage', msg)

    def test_returns_usage_when_user_asks_help(self, _, _1):
        msg = main(['dummy_prog', '--help'])
        assert_in('usage', msg)
 
    @patch('depict.__main__.RepresentationsRecruiter')
    def test_returns_list_of_representations_when_asked_to(self, repr_recruiter_mock, _1, _2):
        msg = main([depict.__main__.__file__, '--list'])
        assert_in('Available representations', msg)
