from .production import *

ROOT_URLCONF = '{{ project_name }}.urls.staging'

WSGI_APPLICATION = '{{ project_name }}.wsgi.staging.application'
