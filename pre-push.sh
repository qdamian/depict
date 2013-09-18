#!/bin/sh
gawk '/^[a-z]/{ section=$0 } /  -/{ if (section~"script|install") { if (system(substr($0, 5))) { exit 1 } } }' .travis.yml
