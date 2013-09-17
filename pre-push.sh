#!/bin/sh
gawk '/^[a-z]/{ section=$0 } /  -/{ if (section~"script|install") { system(substr($0, 5)) } }' .travis.yml
