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

from depict.persistence.html.html_doc import HtmlDoc
from depict.modeling.static_data_notifier import StaticDataNotifier
from depict.model.model import Model

class Html(object):

    def __init__(self, file_set, title, out_filename):
        self.html_doc = HtmlDoc(title, out_filename)
        self.static_data_notifier = StaticDataNotifier(file_set, self.html_doc,
                                                       Model())

    def run(self):
        self.static_data_notifier.run()
        self.html_doc.render()
