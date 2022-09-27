import os

import dj_database_url

from stbcms.settings.dev import ALLOWED_HOSTS
from .base import *

DEBUG = False

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')

ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS', '').split(',')

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

DATABASES = {
    'default': {
        **dj_database_url.config(),
        'CONN_MAX_AGE': 10,
        'CONN_HEALTH_CHECKS': True,
    }
}


try:
    from .local import *
except ImportError:
    pass
