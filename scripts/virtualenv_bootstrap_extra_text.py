import os
import subprocess

dependencies = [
                'mock',
                'nose',
                'nose-parameterized',
                'pylint',
               ]

def after_install(options, home_dir):
    for package in dependencies:
        subprocess.call([os.path.join(home_dir, 'bin', 'pip'), 'install', package])
