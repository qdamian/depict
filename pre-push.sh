#/bin/sh

set -e
pip install -r python/requirements --use-mirrors
npm install
nosetests python
npm test
