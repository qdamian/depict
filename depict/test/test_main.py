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
from depict.main import Depict

@patch('depict.main.DataRetriever')
@patch('depict.main.DataSender')
class TestMain(object):
    def test_it_passes_data_from_retriever_to_sender(self, data_sender,
                                                     data_retriever):
        # Act
        Depict("fake/file").start()

        # Assert
        data_retriever.assert_called_once_with("fake/file",
                                       data_sender.return_value.send_message)

    def test_it_starts_retrieving_data(self, data_sender,
                                       data_retriever):
        # Act
        Depict("dummy)file").start()

        # Assert
        data_retriever.return_value.run.assert_called_once_with()

    def test_it_starts_sending_data(self, data_sender,
                                      data_retriever):
        # Act
        Depict("dummy)file").start()

        # Assert
        data_sender.return_value.start.assert_called_once_with()
