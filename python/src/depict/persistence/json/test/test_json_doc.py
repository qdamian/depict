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

from depict.model.module import Module
from depict.persistence.json.json_doc import JsonDoc
from mock import patch, mock_open
from nose.tools import assert_equal
import json
import unittest
from depict.model.repo import Repo

def assert_equal_json(a, b):
    normalize = lambda json_str: json.dumps(json.loads(json_str))
    assert_equal(normalize(a), normalize(b))

class TestJsonDoc():

    def test_outputs_module_names(self):
        open_mock = mock_open()
        with patch('depict.persistence.json.json_doc.open', open_mock, create=True):
            with patch('depict.persistence.json.json_doc.global_module_repo', Repo()) as module_repo_mock:
                handle = open_mock()

                fake_module1 = Module('fake_module_id1', 'fake_module_name1')
                module_repo_mock.add(fake_module1)
                fake_module2 = Module('fake_module_id2', 'fake_module_name2')
                module_repo_mock.add(fake_module2)

                json_doc = JsonDoc('dummy_filename')
                json_doc.on_collection_completed()

                actual_calls = [call[0][0] for call in handle.write.call_args_list]
                assert_equal_json(''.join(actual_calls), '''
                                      [{"id_": "fake_module_id1",
                                        "dependencies": [],
                                        "type": "Module",
                                        "name": "fake_module_name1"},
                                      {"id_": "fake_module_id2",
                                        "dependencies": [],
                                        "type": "Module",
                                        "name": "fake_module_name2"}]
                                        ''')
