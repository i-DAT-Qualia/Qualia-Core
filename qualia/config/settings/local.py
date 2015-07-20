from .base import *


SECRET_KEY = 'qanur7mbhetm8_f^%ruq9d-l0=ot5e34cqm97bk_j33ucxl7ag'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'django_app',
        'USER': 'django',
        'PASSWORD': 'd15Bb5zo67174yi',
        'HOST': '',
        'PORT': '',
    }
}

STATIC_URL = '/static/'
STATIC_ROOT = '/var/www/static/'
