"""
Custom storage S3 storage backends.
"""
from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    bucket_name = settings.AWS_STATIC_BUCKET_NAME
    custom_domain = settings.AWS_STATIC_CUSTOM_DOMAIN
    bucket_acl = 'public-read'
    default_acl = 'public-read'
    querystring_auth = False
    object_parameters = {
        'CacheControl': 'max-age=86400',
    }
