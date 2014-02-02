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

from contextlib import contextmanager

from depict.data.retriever import Retriever as DataRetriever
from depict.data.sender import Sender as DataSender

class Depict(object):

    def __init__(self):
        self.sender = DataSender()
        self.sender.start()

    def run(self, file_path):
        retriever = DataRetriever(self.sender.send_message)
        retriever.run(file_path)

    @contextmanager
    def trace(self, root_dir_path):
        retriever = DataRetriever(self.sender.send_message)
        with retriever.trace(root_dir_path) as tracer:
            yield tracer

    def stop(self):
        self.sender.stop()

    @property
    def http_port(self):
        return self.sender.server.http_port

