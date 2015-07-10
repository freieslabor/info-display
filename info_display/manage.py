#!/usr/bin/env python
import os
import sys

MSG = """
You are not running in a virtualenv!
Do you know what you are doing?
Type uppercase 'yes': """

if not os.environ.get('VIRTUAL_ENV'):
    while True:
        if raw_input(MSG) == 'YES':
            break

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "info_display.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
