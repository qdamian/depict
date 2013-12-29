#!/usr/bin/env python

from setuptools import setup
import os

FILE_ABSPATH = os.path.abspath(__file__)
os.chdir(os.path.dirname(FILE_ABSPATH))

setup(
    setup_requires=['pbr'],
    pbr=True,
)

