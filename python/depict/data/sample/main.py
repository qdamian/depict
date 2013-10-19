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
import argparse
import time
from util.stopwatch import Stopwatch

logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
LOGGER = logging.getLogger(__name__)

DESCRIPTION = "This is depict's sample program"

def say_hi():
    LOGGER.debug(DESCRIPTION)

def main():
    stopwatch = Stopwatch()
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument('--timeout', type=float,
                     help='Max execution time (msec) that returns success')
    parser.add_argument('--repeat', type=int,
                     help='Say hi 3 times')
    args = parser.parse_args()

    say_hi()

    if args.repeat:
        for _ in range(args.repeat):
            time.sleep(0.5)
            say_hi()

    LOGGER.debug('Elapsed time: %9.2f msec', stopwatch.elapsed_ms())

    if args.timeout:
        if stopwatch.elapsed_ms() > float(args.timeout):
            exit(1)
    exit(0)

if __name__ == '__main__':
    main()
