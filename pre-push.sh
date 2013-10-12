#!/bin/sh
awk '/^[a-z]/{ section=$0 } / *-/{ if (section~"script|install") { if (system(substr($0, 7))) { exit 1 } } }' .travis.yml
