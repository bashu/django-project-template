from .base import *

DEBUG_PROPAGATE_EXCEPTIONS = True

ROOT_URLCONF = '{{ project_name }}.urls.development'

WSGI_APPLICATION = '{{ project_name }}.wsgi.development.application'

CSRF_COOKIE_DOMAIN = None
SESSION_COOKIE_DOMAIN = None
