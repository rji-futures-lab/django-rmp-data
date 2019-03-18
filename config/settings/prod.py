"""
Django project settings for the production environment.
"""
from .base import * # noqa


ALLOWED_HOSTS = [
    'ek4a6i88v6.execute-api.us-east-2.amazonaws.com',
    'rmp.rjifuture.org',
]

INSTALLED_APPS = INSTALLED_APPS + ['storages', ]

AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
AWS_DEFAULT_ACL = None
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
STATIC_URL = "https://%s/static/" % AWS_S3_CUSTOM_DOMAIN
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# RMP_DATA_DIR = os.path.join(ROOT_DIR, 'data', 'rmp')
# RMP_RAW_DATA_DIR = os.path.join(RMP_DATA_DIR, 'raw')
# RMP_PROCESSED_DATA_DIR = os.path.join(RMP_DATA_DIR, 'processed')
