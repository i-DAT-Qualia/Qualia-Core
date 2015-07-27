import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

INSTALLED_APPS = (
    'accounts',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'django.contrib.postgres',
    'tastypie',
    'imagekit',
    'leaflet',
    'provider',
    'provider.oauth2',
    'registration',
    'front'
)

AUTH_USER_MODEL = 'accounts.QualiaUser'

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "tools.context_processors.branding"
)

ROOT_URLCONF = 'config.urls'

WSGI_APPLICATION = 'config.wsgi.application'

LANGUAGE_CODE = 'en-gb'

TIME_ZONE = 'Europe/London'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LEAFLET_CONFIG = {
    'DEFAULT_CENTER': (50.3750391347, -4.13879066706),
    'DEFAULT_ZOOM': 16,
}

CACHES = {
    'default': {
        'BACKEND': 'tools.caches.LargeMemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

# Branding settings
APP_NAME = 'Core'
QUALIA_NAME = 'Core'
LOGO = 'icons/Icon_128.png'
FAVICON = 'icons/favicon.ico'
