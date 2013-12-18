#!/bin/bash

virtualenv --system-site-packages .
bin/pip install -i http://c.pypi.python.org/simple --use-mirrors -e .

echo "TESTING = True" > mypebble/local_settings.py
