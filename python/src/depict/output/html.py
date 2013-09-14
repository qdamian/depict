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

from depict.persistence.html.html_doc import HtmlDoc
from depict.modeling.static_data_notifier import StaticDataNotifier

# pylint:disable = too-few-public-methods
class Html(object):

    def __init__(self, file_set, title, out_filename,
                 def_collection_orchestrator):
        self.html_doc = HtmlDoc(title, out_filename)
        self.static_data_notifier = StaticDataNotifier(file_set, self.html_doc,
                                                    def_collection_orchestrator)

    def run(self):
        self.static_data_notifier.run()
        self.html_doc.render()