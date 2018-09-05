"""
Django project settings for the production environment.
"""
from .base import * # noqa


ALLOWED_HOSTS = [
    # '1q4j4c7dbh.execute-api.us-east-2.amazonaws.com',
    'rmp.rjifuture.org',
]

# TODO: After we workout hosting, switch this to connect to and AWS instance
# running latest version of Postgres
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
