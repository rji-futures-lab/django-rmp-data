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

DATABASES = {
    'default': env.db(), # Raises ImproperlyConfigured exception if DATABASE_URL not in os.environ
}

DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

RMP_DATA_DIR = os.path.join(ROOT_DIR, 'data', 'rmp')
