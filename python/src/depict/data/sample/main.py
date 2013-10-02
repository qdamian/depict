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

import logging
import sys

logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
LOGGER = logging.getLogger(__name__)

def say_hi():
    LOGGER.debug('Hi!')

def say_bye():
    LOGGER.debug('Bye!')

def main():
    LOGGER.debug("This is depict's sample program")
    say_hi()
    say_bye()

if __name__ == '__main__':
    main()
