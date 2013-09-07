#/bin/sh

set -e

# Install
pip install -r python/requirements --use-mirrors
npm install

# Test
pylint --rcfile=python/src/.pylintrc python/src/depict/
nosetests python
npm test
