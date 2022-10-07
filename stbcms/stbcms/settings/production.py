import os

import dj_database_url

from stbcms.settings.dev import ALLOWED_HOSTS
from .base import *



ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS', '').split(',')

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")

AWS_S3_CUSTOM_DOMAIN = os.getenv("AWS_S3_CUSTOM_DOMAIN")

AWS_S3_ENDPOINT_URL = os.getenv("AWS_S3_ENDPOINT_URL")

AWS_S3_REGION_NAME = os.getenv("AWS_S3_REGION_NAME")

AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")

AWS_STORAGE_BUCKET_NAME = os.getenv("AWS_STORAGE_BUCKET_NAME")

AWS_S3_OBJECT_PARAMETERS = {
    "CacheControl": "max-age=86400",
    "ACL": "public-read"
}

DATABASES = {
    'default': {
        **dj_database_url.config(),
        'CONN_MAX_AGE': 10,
        'CONN_HEALTH_CHECKS': True,
    }
}

DEBUG = False

DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/"

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

WAGTAILFRONTENDCACHE = {
    "cloudflare": {
        "BACKEND": "wagtail.contrib.frontend_cache.backends.CloudflareBackend",
        "BEARER_TOKEN": os.getenv("CLOUDFLARE_BEARER_TOKEN"),
        "ZONEID": os.getenv("CLOUDFLARE_ZONEID"),
    }
}

try:
    from .local import *
except ImportError:
    pass
