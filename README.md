# Getting Started

## Debian

    # apt-get install python3-dev python3-pip libxml2-dev libxslt1-dev

## virtualenv

    $ pip install --user --upgrade virtualenv
    $ virtualenv -p python3.5 env
    $ source env/bin/activate
    (env) $ ./setup.py install

### Check if virtualenv is active

    $ printenv | grep VIRTUAL_ENV

### Deactivate virtualenv

    $ deactivate
    
## Run

    (env) $ info-display collectstatic
    (env) $ info-display

## Configuration

    INFO_DISPLAY_DEBUG=0
    INFO_DISPLAY_LOG_LEVEL=INFO  # {DEBUG,INFO,WARN,ERROR,FATAL}
    INFO_DISPLAY_DB=data/db.sqlite3
    (env) $ info-display
