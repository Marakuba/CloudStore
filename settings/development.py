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

MEDIA_URL = '/media/'
ADMIN_MEDIA_PREFIX = '/media/admin/'


STATIC_ROOT = MEDIA_ROOT

STATIC_URL = MEDIA_URL

STATICFILES_DIRS = (
)

INTERNAL_IPS = ('127.0.0.1',)
