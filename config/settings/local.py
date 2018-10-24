"""
Django project settings for developer's local environment.
"""
import os
from .base import * # noqa


DEBUG = True

ALLOWED_HOSTS = [
    'localhost',
    '0.0.0.0',
    '127.0.0.1',
    '.ngrok.io',
]

INSTALLED_APPS = INSTALLED_APPS + ['debug_toolbar',]

MIDDLEWARE = MIDDLEWARE + [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

DATABASES = {
    'default': env.db(), # Raises ImproperlyConfigured exception if DATABASE_URL not in os.environ
}

DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

RMP_DATA_DIR = os.path.join(ROOT_DIR, 'data', 'rmp')
RMP_RAW_DATA_DIR = os.path.join(RMP_DATA_DIR, 'raw')
RMP_PROCESSED_DATA_DIR = os.path.join(RMP_DATA_DIR, 'processed')


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
        },
        'rmp.management': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
