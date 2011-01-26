# -*- coding: utf-8 -*-
import os, sys

def rel(*x):
    return os.path.join(os.path.abspath(os.path.dirname(__file__)), *x)

sys.path.insert(0, rel('..', 'lib'))
sys.path.insert(0, rel('app',))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (('admin', 'admin@elston.ru'),)
MANAGERS = ADMINS
#-------------------------------------------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': rel('database.sqlite'),                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}
#-------------------------------------------------------------------------------
TIME_ZONE = 'Europe/Moscow'
LANGUAGE_CODE = 'ru-RU'

USE_I18N = True
DEFAULT_CHARSET = 'UTF-8'
#SESSION_DURATION = 30 # in minutes
SESSION_COOKIE_NAME = 'session_id'

SITE_ID = 1

SECRET_KEY = 't(mdkda^s5t+pyp(4u_79nr5l^55yd#m0kh9aewg^+7kr8ft*p'

#-------------------------------------------------------------------------------
MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'

AUTHENTICATION_BACKENDS = (
    'accounts.backends.CustomUserBackend',
    #'django.contrib.auth.backends.ModelBackend',
)
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'middleware.EnforceLoginMiddleware',

)
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    #'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.messages',
    'mptt',    
    'feincms',
    'app.accounts',

)
TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",
)
#-------------------------------------------------------------------------------
ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = rel('templates')
MEDIA_ROOT = rel('static')



ADMIN_MEDIA_PREFIX = '/admin_media/'
FEINCMS_ADMIN_MEDIA = '/static/feincms_media/'

MEDIA_URL = '/static/'
LOGIN_URL = '/admin/login/'
PUBLIC_URLS = (
    'favicon.ico',
)
