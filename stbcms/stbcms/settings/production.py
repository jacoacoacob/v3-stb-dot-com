from stbcms.stbcms.settings.dev import ALLOWED_HOSTS
from .base import *

DEBUG = False

ALLOWED_HOSTS = ["localhost"]

try:
    from .local import *
except ImportError:
    pass
