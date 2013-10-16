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

Feature: trace

@trace @help
Scenario: advertise the trace representation 
    When I run depict asking for the list of available representations
    Then I see trace listed

@trace @calls
Scenario: trace function calls
    Given I dumped the sample program provided by depict
    When I run depict with the trace representation
    Then I see the function calls printed

@trace @actors
Scenario: trace actors
    Given I dumped the sample program provided by depict
    When I run depict with the trace representation
    Then I see the class or module each called function belongs to

@trace @modules
Scenario: trace modules
    Given I dumped the sample program provided by depict
    When I run depict with the trace representation
    Then I see the module name for each function call
