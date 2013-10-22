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
from depict.html5.sequence_diagram.sequence_diagram import SequenceDiagram
from depict.html5.sequence_diagram.profile import DESCRIPTION

def main(argv):
    parser = argparse.ArgumentParser(prog='python -m depict.html5'
                                          '.sequence_diagram',
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
    seq_diag = SequenceDiagram(prog.base_path)
    seq_diag.start()
    sys.argv = sys.argv[1:]

    try:
        execfile(prog.abs_path, prog.globals)
    except SystemExit:
        seq_diag.wait()
        seq_diag.stop()
    return ''

if __name__ == '__main__':
    print main(sys.argv)
