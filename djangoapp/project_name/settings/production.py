from .base import *

import os, re

DEBUG = False
SERVE_MEDIA = DEBUG

ADMINS = [
]
MANAGERS = ADMINS

ALLOWED_HOSTS = ['.example.com', 'localhost']

ADMIN_URL = os.environ.get('DJANGO_ADMIN_URL', r'^admin/')

# This ensures that Django will be able to detect a secure connection
# properly on Heroku.
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True

INSTALLED_APPS += [
    'anymail',
    'admin_honeypot',
]

MIDDLEWARE_CLASSES += [
    'localsite.middleware.RemoteAddrMiddleware',
]

import dj_database_url
DATABASES = {
    'default': dj_database_url.config(default='postgres://localhost'),
}
DATABASES['default']['CONN_MAX_AGE'] = 600

DEFAULT_FILE_STORAGE = "localsite.custom_storages.DefaultStorage"

ROOT_URLCONF = '{{ project_name }}.urls.production'

WSGI_APPLICATION = '{{ project_name }}.wsgi.production.application'

MEDIA_ROOT = 'media'
MEDIA_URL = "https://{bucket_name}.s3.amazonaws.com/".format(
    bucket_name = AWS_STORAGE_BUCKET_NAME,
)

IGNORABLE_404_URLS = [
    re.compile(r'^/apple-touch-icon.*\.png$'),
    re.compile(r'^/favicon\.ico$'),
]


## Email / notification settings

ANYMAIL = {
    "MAILGUN_API_KEY": os.environ.get('MAILGUN_API_KEY', "")
}
EMAIL_BACKEND = "anymail.backends.mailgun.MailgunBackend"  # or sendgrid.SendGridBackend, or...


## Cross Site Request Forgery protection

CSRF_COOKIE_SECURE = False
CSRF_COOKIE_HTTPONLY = True


## Session settings

SESSION_COOKIE_SECURE = False
SESSION_COOKIE_HTTPONLY = True


## Logging settings

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console", "mail_admins"],
        }
    }
}
