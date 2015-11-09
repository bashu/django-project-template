from .base import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG
SERVE_MEDIA = DEBUG

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': '127.0.0.1:6379',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}

ROOT_URLCONF = '{{ project_name }}.urls.production'

WSGI_APPLICATION = '{{ project_name }}.wsgi.production.application'

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
