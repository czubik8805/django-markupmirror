"""Test settigs for django-markupmirror."""

import os


TESTS_PATH = os.path.abspath(os.path.dirname(__file__))


def tests_path_to(*parts):
    """Returns absolute path for ``parts`` relative to ``TESTS_PATH``."""
    return os.path.abspath(os.path.join(TESTS_PATH, *parts))


DEBUG = True
TEMPLATE_DEBUG = DEBUG

INSTALLED_APPS = (
    'markupmirror',
    'markupmirror.feincms',
    'markupmirror.tests',
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


# ### coverage / django-coverage

INSTALLED_APPS += (
    'django_coverage',
)

COVERAGE_ADDITIONAL_MODULES = [
    'markupmirror',
]

COVERAGE_PATH_EXCLUDES = [
    r'.hg',
    r'bin',
    r'etc',
    r'fixtures',
    r'media',
    r'static',
    r'templates',
]

COVERAGE_CODE_EXCLUDES = [
    'def __unicode__\(self\):',
    'def get_absolute_url\(self\):',
    'from .* import .*', 'import .*',
    'except ImportError:',
]

COVERAGE_REPORT_HTML_OUTPUT_DIR = tests_path_to(
    os.path.pardir, os.path.pardir, 'docs', '_coverage')
