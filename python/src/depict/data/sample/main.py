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

import logging
import sys
import time
import argparse

DESCRIPTION = "This is depict's sample program"

logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
LOGGER = logging.getLogger(__name__)

def say_hi():
    LOGGER.debug(DESCRIPTION)

class Stopwatch(object):
    def __init__(self):
        self.start_time = time.time()

    def elapsed(self):
        return time.time() - self.start_time

def main():
    stopwatch = Stopwatch()
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument('--timeout', type=float,
                     help='Max execution time (sec) that returns success')
    args = parser.parse_args()

    say_hi()
    LOGGER.debug('Elapsed time: %s sec', stopwatch.elapsed())

    if args.timeout:
        if stopwatch.elapsed() > float(args.timeout):
            exit(1)
    exit(0)

if __name__ == '__main__':
    main()
