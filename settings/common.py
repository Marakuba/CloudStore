# -*- coding: utf-8 -*-

import sys
from path import path
#-------------------------------------------------------------------------------
PROJECT_ROOT = path(__file__).abspath().dirname().dirname()
SITE_ROOT = PROJECT_ROOT.dirname()

sys.path.append(SITE_ROOT)
sys.path.append(PROJECT_ROOT / 'apps')
sys.path.append(PROJECT_ROOT / 'libs')

TEMPLATE_DIRS = [PROJECT_ROOT / 'templates']
MEDIA_ROOT = PROJECT_ROOT / 'media'
UPLOAD_DIR = MEDIA_ROOT / 'photo'

#-------------------------------------------------------------------------------
ROOT_URLCONF = 'urls'
#-------------------------------------------------------------------------------
DEBUG = True
TEMPLATE_DEBUG = DEBUG
#-------------------------------------------------------------------------------
ADMINS = (
          ('trx', '4015555@gmail.com'),
)
MANAGERS = ADMINS
TIME_ZONE = 'Europe/Moscow'
LANGUAGE_CODE = 'ru-RU'
USE_L10N = True
USE_I18N = True
SECRET_KEY = '!5o10g#n)p$oou@u$_xe9d+p*_88ly@47956+h=vnffca2_#o+'

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
    'staticfiles',
    'debug_toolbar',
    'apps.accounts',

)
TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",
)
