"""
Django settings for info_display project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from django.conf import global_settings
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'x=-58f7di+8oaq5+l@04t+02$=5=eiyicf#jvqhpc91&#mzy*^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    # base application
    'info_screen',

    # django suit
    'suit',
    'suit_ckeditor',

    # django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # screens
    'days_without_an_accident',
    'announcer',
    'bus',
)

if DEBUG:
    INSTALLED_APPS += (
        'django_extensions',
    )


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
    'django.core.context_processors.request',
)

ROOT_URLCONF = 'info_display.urls'

WSGI_APPLICATION = 'info_display.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Berlin'

USE_I18N = True

USE_L10N = True

USE_TZ = True

DATETIME_FORMAT = 'D j. N H:i:s'
DATE_FORMAT = 'D j. N'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

# Django Suit
SUIT_CONFIG = {
    'ADMIN_NAME': 'Info Display',
    'HEADER_DATE_FORMAT': 'D j. N',
    'HEADER_TIME_FORMAT': 'H:i',

    'MENU': (
        'sites',
        {
            'app': 'auth',
            'label': 'Auth',
            'icon': 'icon-lock',
            'models': ('user', 'group'),
        },
        '-',
        {
            'app': 'announcer',
            'label': 'Announcer',
            'icon': 'icon-info-sign',
        },
        {
            'app': 'days_without_an_accident',
            'label': 'Days Without An Accident',
            'icon': 'icon-fire',
        },
    ),
}

# info display
INFO_SCREEN_SCREENS = (
    'http://freieslabor.org/blog/',
    'http://freieslabor.org/wiki/Freies_Labor',
    'https://stratum0.org/wiki/Hauptseite',
    'http://www.pengutronix.de/index_de.html',
    '/bus/',
)
