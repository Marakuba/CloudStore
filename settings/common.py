# -*- coding: utf-8 -*-

import sys
from path import path

PROJECT_ROOT = path(__file__).abspath().dirname().dirname()

SITE_ROOT = PROJECT_ROOT.dirname()

sys.path.append(SITE_ROOT)
sys.path.append(PROJECT_ROOT / 'apps')
sys.path.append(PROJECT_ROOT / 'libs')

MEDIA_ROOT = PROJECT_ROOT / 'media'
UPLOAD_DIR = MEDIA_ROOT / 'photo'
TEMPLATE_DIRS = [PROJECT_ROOT / 'templates']

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
          ('trx', '4015555@gmail.com'),
)

MANAGERS = ADMINS

TIME_ZONE = 'Europe/Moscow'

LANGUAGE_CODE = 'ru-RU'

USE_L10N = True

USE_I18N = True

SECRET_KEY = '!5o10g#n)p$oou@u$_xe9d+p*_88ly@47956+h=vnffca2_#o+'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
)

ROOT_URLCONF = 'cloudstore.urls'

MIDDLEWARE_CLASSES = (
    #'debug_toolbar.middleware.DebugToolbarMiddleware',
    #'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.cache.FetchFromCacheMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
)

INSTALLED_APPS = (
    #'admin_tools',
    #'admin_tools.theming',
    #'admin_tools.menu',
    #'admin_tools.dashboard',

    'django.contrib.admin',
    'django.contrib.auth',
    #'django.contrib.comments',
    'django.contrib.contenttypes',
    #'django.contrib.flatpages',
    #'django.contrib.markup',
    'django.contrib.sessions',
    #'django.contrib.sites',
    
    #'ajax_validation',
    #'autocomplete',
    'debug_toolbar',
    #'piston',
    'south',
    #'staticfiles',
    #'tagging',
    #'uni_form',
)

#ADMIN_TOOLS_MENU = 'cloudstore.menu.CustomMenu'

#ADMIN_TOOLS_INDEX_DASHBOARD = 'cloudstore.dashboard.CustomIndexDashboard'
