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

from depict.model.entity.module import Module
from depict.persistence.sqlite.module_table import ModuleTable
import sqlite3
from nose.tools import assert_true

class TestModuleTable(object):
    def setUp(self):
        self.connection = sqlite3.connect(':memory:')
        self.module_table = ModuleTable(self.connection)
        self.module_table.create()
    
    def test_module_table_creation(self):
        self.connection.execute('SELECT id, name FROM module')

    def test_module_dependency_table_creation(self):
        self.connection.execute('SELECT importer_id, imported_id FROM module_dependency')

    def test_inserts_a_module(self):
        fake_module = Module('fake_module_id', 'fake_module_name')
        self.module_table.insert(fake_module)
        cursor = self.connection.cursor()
        cursor.execute('''SELECT id, name FROM module
                          WHERE id = 'fake_module_id' AND
                          name = 'fake_module_name' ''')
        assert_true(cursor.fetchone())

    def test_inserts_module_dependencies(self):
        fake_module = Module('fake_module_id', 'fake_module_name')
        fake_dependency = Module('fake_dependency_id', 'fake_dependency_name')
        fake_module.depends_on(fake_dependency)
        self.module_table.insert(fake_module)
        cursor = self.connection.cursor()
        cursor.execute('''SELECT importer_id, imported_id FROM module_dependency
                          WHERE importer_id = 'fake_module_id' AND
                          imported_id = 'fake_dependency_id' ''')
        assert_true(cursor.fetchone())

    def test_ignores_integry_error_of_repeated_dependencies(self):
        fake_module = Module('fake_module_id', 'fake_module_name')
        fake_dependency = Module('fake_dependency_id', 'fake_dependency_name')
        fake_module.depends_on(fake_dependency)
        self.module_table.insert(fake_module)
        self.module_table.insert(fake_module)
        cursor = self.connection.cursor()
        cursor.execute('''SELECT importer_id, imported_id FROM module_dependency
                          WHERE importer_id = 'fake_module_id' AND
                          imported_id = 'fake_dependency_id' ''')
        assert_true(cursor.fetchone())