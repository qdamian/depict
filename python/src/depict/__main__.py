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

from depict.cli.representations_recruiter import RepresentationsRecruiter
from shutil import copytree
from os import path
import argparse
import sys

# pylint:disable = invalid-name

def parse_args(argv):
    description = 'Create representations of a python program'
    epilog = 'For more information, see ' \
             'https://github.com/qdamian/depict/wiki/User-guide'
    parser = argparse.ArgumentParser(prog='python -m depict',
                                     description=description,
                                     epilog=epilog)
    parser.add_argument('-l', '--list-representations', action='store_true',
                        help='list available representations')
    parser.add_argument('-d', '--dump-sample-program', action='store',
                        const='sample', nargs='?',
                        help='generate a sample program in the given directory')
    args = parser.parse_args(argv)
    return [parser, args]

def list_repr(base_path):
    return RepresentationsRecruiter(base_path).run()

def format_repr(repr_desc):
    msg = ['Available representations:']
    msg += []
    for item in repr_desc:
        msg += ['\t%s : %s' % (item[0], item[1])]
    return '\n'.join(msg)

def dump_sample_program(base_path, dst_path):
    src_path = path.join(base_path, 'depict', 'data', 'sample')
    copytree(src_path, dst_path)
    return "Generated '%s'" % dst_path

def main(argv):
    [parser, args] = parse_args(argv[1:])
    base_path = path.abspath(path.dirname(path.dirname(sys.argv[0])))
    if args.list_representations:
        return format_repr(list_repr(base_path))
    elif args.dump_sample_program:
        return dump_sample_program(base_path, args.dump_sample_program)
    return parser.format_help()

if __name__ == '__main__':
    print main(sys.argv)
