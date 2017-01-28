#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='info-display',
    version='0.0',
    description='',
    url='https://github.com/freieslabor/info-display',
    author='Freies Labor',
    license='MPL-2.0',
    packages=find_packages(),
    scripts=[
        'bin/info-display-cli',
    ],
    install_requires=[
        'Django>=1.8,<1.9',
        'django-extensions==1.5.2',
        'django-suit==0.2.13',
        'django-suit-ckeditor==0.0.2',
        'lxml==3.4.3',
        'python-dateutil==2.4.2',
        'icalendar==3.9.0',
    ],
)
