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

from depict.cli.representations_recruiter import get_representations
import argparse
from os import path
import sys
import importlib

# pylint:disable = invalid-name

def parse_args(argv):
    description = 'Create representations of a python program'
    epilog = \
          'For more info see: https://github.com/qdamian/depict/wiki/User-guide'
    parser = argparse.ArgumentParser(prog='python -m depict',
                                     description=description,
                                     epilog=epilog)
    parser.add_argument('--list', action='store_true',
                        help='list available representations')
    args = parser.parse_args(argv)
    return [parser, args]

def list_repr(program_path):
    base_path = path.abspath(path.dirname(path.dirname(program_path)))
    modules = get_representations(base_path)
    repr_dict = {}
    for mod in modules:
        try:
            imported_mod = importlib.import_module(mod.name + '.profile')
            repr_dict[mod.name] = imported_mod.DESCRIPTION
        except ImportError:
            pass
    return repr_dict

def format_repr(repr_dict):
    msg = ['Available representations:']
    msg += []
    for key in repr_dict:
        msg += ['\n%s : %s' % (key, repr_dict[key])]
    return '\n'.join(msg)

def main(argv):
    [parser, args] = parse_args(argv[1:])
    if args.list:
        return format_repr(list_repr(argv[0]))
    return parser.format_help()

if __name__ == '__main__':
    print main(sys.argv)