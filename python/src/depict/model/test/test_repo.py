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

from depict.model.repo import Repo
from mock import Mock
import unittest
from nose.tools import assert_raises

class TestRepo(unittest.TestCase):
    def test_add_one_element(self):
        repo = Repo()
        in_element = Mock()
        in_element.id_ = 'fake_id'
        repo.add(in_element)
        out_element = repo.get_by_id('fake_id')
        self.assertEqual(in_element, out_element)

    def test_add_two_elements(self):
        repo = Repo()
        in_element1 = Mock()
        in_element1.id_ = 'fake_id1'
        in_element2 = Mock()
        in_element2.id_ = 'fake_id2'
        repo.add(in_element1)
        repo.add(in_element2)
        out_element1 = repo.get_by_id('fake_id1')
        self.assertEqual(in_element1, out_element1)
        self.assertNotEqual(in_element2, out_element1)

    def test_get_by_id_throws_exception_if_key_is_not_found(self):
        repo = Repo()
        assert_raises(KeyError, repo.get_by_id, 'inexistent_id')

    def test_get_by_names_throws_exception_if_key_is_not_found(self):
        repo = Repo()
        assert_raises(KeyError, repo.get_by_name, 'inexistent_name')

    def test_get_all_returns_all_elements(self):
        repo = Repo()
        in_element1 = Mock()
        in_element1.id_ = 'fake_id1'
        repo.add(in_element1)
        in_element2 = Mock()
        in_element2.id_ = 'fake_id2'
        repo.add(in_element2)
        self.assertEqual(set(repo.get_all()), set([in_element1, in_element2]))

    def test_get_an_element_by_name(self):
        repo = Repo()
        in_element1 = Mock()
        in_element1.id_ = 'fake_id1'
        in_element1.name = 'fake_name1'
        repo.add(in_element1)
        in_element2 = Mock()
        in_element2.id_ = 'fake_id2'
        in_element2.name = 'fake_name2'
        repo.add(in_element2)
        self.assertEqual(repo.get_by_name('fake_name1'), in_element1)
