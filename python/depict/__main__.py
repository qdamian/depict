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

from depict.cli.representations_recruiter import RepresentationsRecruiter
from shutil import copytree
from os import path
import argparse
import sys
from argparse import RawTextHelpFormatter

# pylint:disable = invalid-name

def parse_args(argv):
    description = 'Create representations of a python program'

    user_guide_link = 'For more info, see ' \
                      'https://github.com/qdamian/depict/wiki/User-guide'

    copyright_notice = 'depict Copyright (C) 2013, Damian Quiroga\n' \
                       'This is free software available under GPLv3 license'

    epilog = user_guide_link + '\n\n' + copyright_notice

    parser = argparse.ArgumentParser(prog='python -m depict',
                                     description=description,
                                     epilog=epilog,
                                     formatter_class=RawTextHelpFormatter)
    parser.add_argument('-l', '--list', action='store_true',
                        help='list available representations')
    parser.add_argument('-s', '--sample', action='store',
                        const='sample', nargs='?',
                        help='dump a sample program in the given directory')
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
    base_path = path.abspath(path.dirname(path.dirname(argv[0])))
    if args.list:
        return format_repr(list_repr(base_path))
    elif args.sample:
        return dump_sample_program(base_path, args.sample)
    return parser.format_help()

if __name__ == '__main__':
    print main(sys.argv)
