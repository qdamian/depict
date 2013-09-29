#!/bin/bash
rm *.out *.json *.db *.html
for f in manual_test/*; do python $f/main.py; done
ls -l *.out *.json *.db *.html
