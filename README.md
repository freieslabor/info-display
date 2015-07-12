# Getting Started

## Debian

    # apt-get install python3-dev python3-pip libxml2-dev libxslt1-dev

## virtualenv

    $ pip install --user --upgrade virtualenv
    $ virtualenv -p python3 env
    $ source env/bin/activate
    $ pip install -r REQUIREMENTS.txt

### Check if virtualenv is active

    $ printenv | grep VIRTUAL_ENV

### Deactivate virtualenv

    $ deactivate
