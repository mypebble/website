#!/bin/bash

bin/python mypebble/manage.py collectstatic --noinput
bin/python mypebble/manage.py syncdb --noinput
bin/python mypebble/manage.py migrate --all --noinput
