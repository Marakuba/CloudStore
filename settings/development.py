# -*- coding: utf-8 -*-

from common import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', 
        'NAME': 'cloudstore_main',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
} 

SITE_ID = 1


#ADMIN_MEDIA_PREFIX = '/media/admin/'
ADMIN_MEDIA_PREFIX = '/admin_media/'
FEINCMS_ADMIN_MEDIA = '/media/feincms_media/'

MEDIA_URL = '/media/'
LOGIN_URL = '/admin/login/'
PUBLIC_URLS = (
    'favicon.ico',
)

STATIC_ROOT = MEDIA_ROOT
STATIC_URL = MEDIA_URL
STATICFILES_DIRS = (
)

INTERNAL_IPS = ('127.0.0.1',)
