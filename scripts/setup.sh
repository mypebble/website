#!/bin/bash

echo 'trying to nuke the db'
sudo -u postgres dropdb mypebble_cms
echo '... and recreate'
sudo -u postgres createdb -E UTF8 -O pebble mypebble_cms -T template0

bin/python mypebble/manage.py syncdb
bin/python mypebble/manage.py migrate

exit 0
