#!/bin/bash

bin/python mypebble/manage.py syncdb
bin/python mypebble/manage.py migrate --all
