from .base import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG
SERVE_MEDIA = DEBUG

}

ROOT_URLCONF = '{{ project_name }}.urls.production'

WSGI_APPLICATION = '{{ project_name }}.wsgi.production.application'

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
