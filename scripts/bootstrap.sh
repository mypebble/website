#!/bin/bash

virtualenv --system-site-packages .
bin/pip install --use-mirrors -e .

echo "TESTING = True" > mypebble/local_settings.py
