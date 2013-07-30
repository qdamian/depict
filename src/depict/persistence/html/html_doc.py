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

import pyratemp

class HtmlDoc(object):
    header_template = '''
    <!doctype html>
    <html lang=en>
    <meta charset=utf-8>
    <title>@!title!@</title>
    <body>
    <li>Modules
      <ul>'''

    module_template = '''
        <li>@!module_name!@</li>'''
    
    footer_template = '''
      </ul>
    </li>    
    '''

    def __init__(self, title, out_filename):
        self.out_filename = out_filename
        header_temp = pyratemp.Template(HtmlDoc.header_template)
        self.html_content = header_temp(title=title)
    
    def on_module(self, module):
        module_temp = pyratemp.Template(HtmlDoc.module_template)
        self.html_content += module_temp(module_name=module.name)

    def render(self):
        footer_temp = pyratemp.Template(HtmlDoc.footer_template)
        self.html_content += footer_temp()
        with open(self.out_filename, 'w') as out_file:
            out_file.write(self.html_content)
    
