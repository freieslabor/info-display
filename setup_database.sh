#!/bin/bash

set -x

rm db.sqlite3 &> /dev/null
./manage.py migrate
./manage.py loaddata login_data.json station_data.json calendar_data.json
