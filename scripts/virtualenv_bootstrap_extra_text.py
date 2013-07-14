import os
import subprocess

def after_install(options, home_dir):
    subprocess.call([os.path.join(home_dir, 'bin', 'pip'), 'install', 'mock'])
