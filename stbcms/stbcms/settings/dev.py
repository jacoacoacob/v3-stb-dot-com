from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-(2a8=eq$492$15x-!ea3n*s4=ru8o7m(47h02=8r$mp&4j(x8u"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

# Setup `django-tailwind`
# https://django-tailwind.readthedocs.io/en/latest/installation.html
TAILWIND_APP_NAME = "theme"
INTERNAL_IPS = [
    "127.0.0.1",
]
INSTALLED_APPS += [
    "tailwind",
    "theme",
    "django_browser_reload"
]
MIDDLEWARE += [
    "django_browser_reload.middleware.BrowserReloadMiddleware"
]
# End setup `django-tailwind`


EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


try:
    from .local import *
except ImportError:
    pass
