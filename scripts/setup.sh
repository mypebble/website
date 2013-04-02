#!/bin/bash

echo 'trying to nuke the db'
sudo -u postgres dropdb mypebble_cms
echo '... and recreate'
sudo -u postgres createdb -E UTF8 -O pebble mypebble_cms -T template0

scripts/syncdb.sh

exit 0
