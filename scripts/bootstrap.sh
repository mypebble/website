#!/bin/bash

virtualenv --system-site-packages .
bin/pip install -i http://pypi.talktopebble.co.uk --use-mirrors -e .

echo "TESTING = True" > mypebble/local_settings.py
