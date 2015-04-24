# Getting Started

## Debian

    # apt-get install python-dev python-pip libxml2-dev libxslt1-dev

## virtualenv

    $ pip install --user --upgrade virtualenv
    $ virtualenv env
    $ source env/bin/activate
    $ pip install -r REQUIREMENTS.txt

### Check if virtualenv is active

    $ printenv | grep VIRTUAL_ENV

### Deactivate virtualenv

    $ deactivate
