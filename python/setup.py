#!/usr/bin/env python

from setuptools import setup
import os

abspath = os.path.abspath(__file__)
os.chdir(os.path.dirname(abspath))

setup(
    setup_requires=['pbr'],
    pbr=True,
)

