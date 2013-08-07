#!/usr/bin/env python

import virtualenv, textwrap
with open('virtualenv_bootstrap_extra_text.py') as extra_text_file:
    extra_text = extra_text_file.readlines()

output = virtualenv.create_bootstrap_script(textwrap.dedent(''.join(extra_text)))
f = open('../bootstrap.py', 'w').write(output)
