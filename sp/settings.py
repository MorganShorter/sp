"""
Django settings for sp project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_DIR = os.path.join(os.path.dirname(__file__), '..')
project_dir = lambda p: os.path.join(PROJECT_DIR, p)

SITE_DOMAIN = "ec2-54-215-172-148.us-west-1.compute.amazonaws.com"

TEMPLATE_DIRS = (
    BASE_DIR + '/templates'
)

EMAIL_HOST = '127.0.0.1'
DEFAULT_FROM_EMAIL = 'noreply@ec2-54-215-172-148.us-west-1.compute.amazonaws.com"'
SERVER_EMAIL = 'noreply@ec2-54-215-172-148.us-west-1.compute.amazonaws.com"'
SITE_ID = 1
SITE_NAME = 'sp'
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'oisdjfoi834j98t6hweg8vsn;ldkfm123095ruy3290478ty3h9p-wer8g0[yua9eg0924jiokl$%^&*('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']

ADMINS = (
    ('debug django sp', 'root@localhost'),
)
# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.comments',
    'django.contrib.humanize',
    'django.contrib.flatpages',
    'raven.contrib.django.raven_compat',
    'registration',
    'compressor',
    'south',
    'mathfilters',
    'frontend',
    'colorfield',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
)

ROOT_URLCONF = 'sp.urls'

WSGI_APPLICATION = 'sp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'smartpractice',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-au'

TIME_ZONE = 'Australia/Melbourne'

# Webodt magic, use Abiword backend
WEBODT_CONVERTER = 'webodt.converters.abiword.AbiwordODFConverter'
#  Where you want to store your .odt templates. Webodt does not know how to use standard Django template loaders, 
#  Directory to store your odt templates (sure enough, its possible to use the same directory where all other templates are stored):
WEBODT_TEMPLATE_PATH = '.../webodt/templates/'

USE_I18N = False
USE_L10N = False
USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = project_dir('static_cache')

MEDIA_URL = '/media/'
MEDIA_ROOT = project_dir('media')

STATICFILES_DIRS = (
    project_dir("static"),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder'
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

MESSAGE_STORAGE = 'django.contrib.messages.storage.fallback.FallbackStorage'

SKIP_SOUTH_TESTS = True

DATE_FORMAT = 'j F Y'
DATETIME_FORMAT = 'Y-m-d H:i'

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

COMPRESS_CSS_FILTERS = [
    #creates absolute urls from relative ones
    'compressor.filters.css_default.CssAbsoluteFilter',
    #css minimizer
    'compressor.filters.cssmin.CSSMinFilter'
]

COMPRESS_JS_FILTERS = [
    'compressor.filters.jsmin.JSMinFilter'
]

COMPRESS_ROOT = PROJECT_DIR
COMPRESS_OUTPUT_DIR = 'compressed'
COMPRESS_ENABLED = True
COMPRESS_PARSER = 'compressor.parser.HtmlParser'

TAX_PERCENT = 10

AUTH_USER_MODEL = 'frontend.SPUser'

try:
    from .local_settings import *
except ImportError:
    pass