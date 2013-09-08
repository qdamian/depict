#!/usr/bin/env python

import os
import sys

import depict

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

packages = [
    'depict',
    'depict.collection',
    'depict.collection.dynamic',
    'depict.collection.static',
    'depict.model',
    'depict.modeling',
    'depict.output',
    'depict.output.toy',
    'depict.persistence',
    'depict.persistence.html',
    'depict.persistence.json',
    'depict.persistence.sqlite',
]

requires = [
    "formic >= 0.9beta8",
    "pyratemp >= 0.3.1",
    "logilab-astng >= 0.24.3",
]

setup(
    name='depict',
    version=depict.__version__,
    description='Create representations on a python program.',
    long_description=open('README.rst').read(),
    author='Damian Quiroga',
    author_email='qdamian@gmail.com',
    url='https://github.com/qdamian/depict',
    packages=packages,
    package_data={'': ['../../COPYING']},
    package_dir={'depict': 'depict'},
    include_package_data=True,
    install_requires=requires,
    license=open('../../COPYING').read(),
    zip_safe=False,
    classifiers=(
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',

    ),
)
