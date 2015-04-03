#!/bin/bash

set -x

rm db.sqlite3 &> /dev/null
./manage.py syncdb --noinput
./manage.py loaddata login_data.json
