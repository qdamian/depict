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

Feature: help

@help
Scenario: provide inline help
    When I run depict with incorrect options
    Then I see basic usage information
    And I see a link to the user guide
    And I see a copyright notice

@help
Scenario: provide a built-in sample program
    Given I dumped the sample program provided by depict
    When I run the sample program
    Then it executes successfully