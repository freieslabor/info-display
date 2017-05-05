info-display
############

Development Environment
=======================

Setup
-----

::

    # apt-get install python3-dev python3-venv libxml2-dev libxslt1-dev
    $ python3.5 -m venv env
    $ source scripts/debug-env.sh
    $ source env/bin/activate
    (env) $ pip install -e .
    (env) $ info-display-cli migrate


Run
---

::

    $ source scripts/debug-env.sh
    $ source env/bin/activate
    (env) $ info-display
