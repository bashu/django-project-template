from .base import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG
SERVE_MEDIA = DEBUG

import dj_database_url
DATABASES = {
    'default': dj_database_url.config(default='postgres://localhost'),
}

ROOT_URLCONF = '{{ project_name }}.urls.production'

WSGI_APPLICATION = '{{ project_name }}.wsgi.production.application'

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
