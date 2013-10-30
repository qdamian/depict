#region GPLv3 notice
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
#endregion

import argparse
import sys

from depict.cli.program_env_emulator import ProgramEnvEmulator
from depict.txt.trace.trace import Trace
from depict.txt.trace.profile import DESCRIPTION

def main(argv):
    parser = argparse.ArgumentParser(prog='python -m depict.txt.trace',
                                     description=DESCRIPTION)
    parser.add_argument('args', nargs='*',
                        help='program read from script file')

    [namespace, _] = parser.parse_known_args(argv[1:])

    try:
        if namespace.help:
            return parser.format_help()
    except AttributeError:
        pass

    prog = ProgramEnvEmulator(argv)
    trace_repr = Trace(prog.base_path)
    trace_repr.start()
    sys.argv = sys.argv[1:]

    try:
        execfile(prog.abs_path, prog.globals)
    except SystemExit:
        trace_repr.stop()
    return ''

if __name__ == '__main__':
    print main(sys.argv)
