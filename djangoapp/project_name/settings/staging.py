from .base import *

DEBUG_PROPAGATE_EXCEPTIONS = True

ROOT_URLCONF = '{{ project_name }}.urls.staging'

WSGI_APPLICATION = '{{ project_name }}.wsgi.staging.application'

