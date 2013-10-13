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

import argparse
import sys

from depict.cli.program_env_emulator import ProgramEnvEmulator
from depict.txt.trace import Trace


# pylint:disable = exec-used

def parse_args(argv):
    description = 'Trace the program execution'
    parser = argparse.ArgumentParser(prog='python -m depict.txt.trace',
                                     description=description)
    parser.add_argument('args', nargs='*',
                        help='program read from script file')
    args = parser.parse_args(argv)
    return [parser, args]

def main(argv):
    [parser, args] = parse_args(argv[1:])
    if not args.args:
        return parser.format_help()

    prog = ProgramEnvEmulator(argv)
    trace_repr = Trace('.')
    trace_repr.start()
    sys.argv = sys.argv[1:]
    exec prog.code in prog.globals, prog.globals
    trace_repr.stop()
    return ''

if __name__ == '__main__':
    print main(sys.argv)