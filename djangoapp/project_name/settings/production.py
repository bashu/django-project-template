from .base import *

import os

DEBUG = False
SERVE_MEDIA = DEBUG

ADMINS = [
]
MANAGERS = ADMINS

ALLOWED_HOSTS = ['.example.com', 'localhost']

# This ensures that Django will be able to detect a secure connection
# properly on Heroku.
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True


# Application definition

INSTALLED_APPS += [
    'anymail',
    'admin_honeypot',
#	'raven.contrib.django.raven_compat',
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

MEDIA_URL = "https://{bucket_name}.s3.amazonaws.com/".format(
    bucket_name = AWS_STORAGE_BUCKET_NAME,
)

IGNORABLE_404_URLS = [
    re.compile(r'^/apple-touch-icon.*\.png$'),
    re.compile(r'^/favicon\.ico$'),
]


## Email / notification settings

ANYMAIL = {
    'AMAZON_SES_CLIENT_PARAMS': {
        'aws_access_key_id': AWS_ACCESS_KEY_ID,
        'aws_secret_access_key': AWS_SECRET_ACCESS_KEY,
        'region_name': 'us-east-1',
    },
}
EMAIL_BACKEND = "anymail.backends.mailgun.MailgunBackend"  # or sendgrid.SendGridBackend, or...


## Raven / Sentry settings

if 'raven.contrib.django.raven_compat' in INSTALLED_APPS:
	if os.environ.get('SENTRY_DSN', None):
	    RAVEN_CONFIG = {
    	    'dsn': os.environ.get('SENTRY_DSN'),
        	# If you are using git, you can also automatically configure the
	        # release based on the git info.
	        'release': __version__,
	    }


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
