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

from depict.cli.representations_recruiter import RepresentationsRecruiter
from nose.tools import *
from mock import patch, MagicMock, Mock, ANY, PropertyMock
from depict.model.entity.module import Module
from depict.model.model import Model

@patch('depict.cli.representations_recruiter.StaticDataNotifier')
class TestRepresentationsRecruiter(object):
    def setUp(self):
        self.static_data_mock = Mock()
        self.fake_model = Model()
        self.model_patcher = patch('depict.cli.representations_recruiter.Model',
                             return_value=self.fake_model, autospec=True)
        self.model_patcher.start()

        self.importlib_mock = Mock()
        self.fake_imported_module = Mock()
        self.fake_imported_module.DESCRIPTION = 'fake description'
        self.importlib_patcher = patch('depict.cli.representations_recruiter.importlib.import_module', autospec=True)
        self.import_module_mock = self.importlib_patcher.start()
        self.import_module_mock.return_value = self.fake_imported_module

    def tearDown(self):
        self.model_patcher.stop()
        self.importlib_patcher.stop()

    def test_returns_an_empty_list_if_it_cannot_find_representations(self, static_data_mock):
        representations_recruiter = RepresentationsRecruiter('dummy_base_path')
        assert_equal(representations_recruiter.run(), [])

    def test_returns_a_single_representation(self, static_data_mock):
        self.fake_model.modules.add(Module('mod_id1', 'mod.fake.name1'))
        representations_recruiter = RepresentationsRecruiter(MagicMock())
        assert_equal(representations_recruiter.run(), [('mod.fake.name1', ANY)])

    def test_returns_representations_ordered_alphabetically(self, static_data_mock):
        self.fake_model.modules.add(Module('mod_id1', 'mod.fake.name1'))
        self.fake_model.modules.add(Module('mod_id2', 'mod.fake.name2'))
        self.fake_model.modules.add(Module('mod_id3', 'mod.fake.name3'))
        representations_recruiter = RepresentationsRecruiter('dummy_base_path')
        expected_result = [('mod.fake.name1', ANY),
                           ('mod.fake.name2', ANY),
                           ('mod.fake.name3', ANY)]
        assert_equal(representations_recruiter.run(), expected_result)

    def test_returns_representation_description(self, static_data_mock):
        self.fake_model.modules.add(Module('mod_id1', 'mod.fake.name1'))
        representations_recruiter = RepresentationsRecruiter(MagicMock())

        actual_result = representations_recruiter.run()

        self.import_module_mock.assert_called_once_with('mod.fake.name1.profile')
        assert_equal(actual_result, [('mod.fake.name1', 'fake description')])

    def test_ignores_import_errors(self, static_data_mock):
        self.fake_model.modules.add(Module('mod_id1', 'mod.fake.name1'))
        representations_recruiter = RepresentationsRecruiter(MagicMock())
        self.import_module_mock.side_effect = ImportError

        actual_result = representations_recruiter.run()

        assert_equal(actual_result, [])
