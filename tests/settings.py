"""Test settigs for django-markupmirror."""
from __future__ import absolute_import, unicode_literals
import os


TESTS_PATH = os.path.abspath(os.path.dirname(__file__))


def tests_path_to(*parts):
    """Returns absolute path for ``parts`` relative to ``TESTS_PATH``."""
    return os.path.abspath(os.path.join(TESTS_PATH, *parts))


DEBUG = True
TEMPLATE_DEBUG = DEBUG

SECRET_KEY = 'abcdefghijklmnopqrstuvwxyz'

INSTALLED_APPS = (
    'django.contrib.contenttypes',
    'markupmirror',
    'markupmirror.feincms',
    'tests',
)

ROOT_URLCONF = 'tests.urls'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'markupmirror.db',
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'markupmirror-tests',
        'KEY_PREFIX': 'markupmirror-tests',
        'TIMEOUT': 300,
    }
}

MEDIA_ROOT = tests_path_to('media')
MEDIA_URL = '/media/'
STATIC_ROOT = tests_path_to('static')
STATIC_URL = '/media/'

USE_TZ = True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'handlers': {
        'simple': {
            'level': 'ERROR',
            'class': 'logging.StreamHandler',
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['simple'],
            'level': 'ERROR',
            'propagate': False,
        },
    }
}

# ### django-markupmirror

MARKUPMIRROR_DEFAULT_MARKUP_TYPE = 'markdown'

MARKUPMIRROR_IGNORE_DEFAULT_TYPES = False


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
