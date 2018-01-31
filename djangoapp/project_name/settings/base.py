"""
Django settings for {{ project_name }} project.

Generated by 'django-admin startproject' using Django {{ django_version }}.

For more information on this file, see
https://docs.djangoproject.com/en/{{ docs_version }}/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

from .. import __version__

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/{{ docs_version }}/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
from django.utils.crypto import get_random_string
SECRET_KEY = os.environ.get("SECRET_KEY", get_random_string(
    50, "abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)"))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

SERVE_MEDIA = True

ALLOWED_HOSTS = []

DJANGO_THEME = 'default'

INTERNAL_IPS = ['127.0.0.1']

SITE_NAME = 'example.com'
SITE_DOMAIN = 'example.com'
SITE_ID = 1

ADMIN_URL = r'^admin/'


# Application definition

DJANGO_APPS = [
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.sessions',
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    'django.contrib.sites',
]

EXTERNAL_APPS = [
    'cachalot',
    
    'django_extensions',
    'djangobower',
    'pipeline',
    
    'robots',
]

PROJECT_APPS = [
    'localsite',
]

INSTALLED_APPS = DJANGO_APPS + EXTERNAL_APPS + PROJECT_APPS

MIDDLEWARE_CLASSES = [
    'django.middleware.common.BrokenLinkEmailsMiddleware',

    # 'django.middleware.cache.UpdateCacheMiddleware',

    'django.middleware.http.ConditionalGetMiddleware',
    'pipeline.middleware.MinifyHTMLMiddleware',
    
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    
    # 'django.middleware.cache.FetchFromCacheMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates', DJANGO_THEME),
        ],
        'OPTIONS': {
            'loaders': [
                ('django.template.loaders.cached.Loader', [
                    'django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader',
                ]),
            ],
            'context_processors': [
                'django.template.context_processors.tz',
                'django.template.context_processors.i18n',
                'django.template.context_processors.debug',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'localsite.context_processors.localsite_settings',
            ],
        },
    },
]


# Database
# https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '..', '..', 'databases', 'db.sqlite3'),
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': os.environ.get('REDIS_URL', '127.0.0.1:6379'),
        'TIMEOUT': 60 * 60 * 24,
        'VERSION': __version__,
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    },
    # Long cache timeout for staticfiles, since this is used heavily by the optimizing storage.
    'staticfiles': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'staticfiles',
        'TIMEOUT': 60 * 60 * 24 * 365,
    },
}

DJANGO_REDIS_IGNORE_EXCEPTIONS = True
CACHE_MIDDLEWARE_SECONDS = 60 * 60


# Internationalization
# https://docs.djangoproject.com/en/{{ docs_version }}/topics/i18n/

LANGUAGE_CODE = 'en-us'

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/{{ docs_version }}/howto/static-files/

MEDIAFILES_LOCATION = 'media'

# Absolute filesystem path to the directory that will hold user-uploaded files.
MEDIA_ROOT = os.path.join(os.path.join(BASE_DIR, '..'), '..', MEDIAFILES_LOCATION)

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
MEDIA_URL = '/media/'

STATICFILES_LOCATION = 'staticfiles'

# Absolute path to the directory static files should be collected to.
STATIC_ROOT = os.path.join(os.path.join(BASE_DIR, '..'), '..', STATICFILES_LOCATION)

STATIC_HOST = os.environ.get('DJANGO_STATIC_HOST', '')
STATIC_URL = STATIC_HOST + '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static', DJANGO_THEME),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'djangobower.finders.BowerFinder',
    'pipeline.finders.PipelineFinder',
)

STATICFILES_STORAGE = 'localsite.custom_storages.GzipManifestPipelineStorage'

MIGRATION_MODULES = {
}

USE_ETAGS = True


## AWS / S3 settings

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID', "")
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY', "")
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME', "")
AWS_AUTO_CREATE_BUCKET = True

AWS_REDUCED_REDUNDANCY = False
AWS_QUERYSTRING_AUTH = False
AWS_IS_GZIPPED = False

AWS_S3_FILE_OVERWRITE = False
AWS_S3_SECURE_URLS = True

AWS_HEADERS = {
    'Access-Control-Allow-Origin': '*',
    'Cache-Control': 'public, max-age=%d' % (7 * 86400),
}


## Email / notification settings

CONTACT_EMAIL = 'support@%s' % SITE_DOMAIN
DEFAULT_FROM_EMAIL = SERVER_EMAIL = CONTACT_EMAIL

EMAIL_SUBJECT_PREFIX = "[%s] " % SITE_NAME

EMAIL_HOST = os.environ.get('EMAIL_HOST', 'localhost')
EMAIL_PORT = os.environ.get('EMAIL_PORT', 25)
if os.environ.get('EMAIL_HOST_USER', None):
    EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', '')
if os.environ.get('EMAIL_HOST_PASSWORD', None):
    EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', '')


## Cross Site Request Forgery protection

CSRF_COOKIE_DOMAIN = '.%s' % SITE_DOMAIN


## Sessions settings

SESSION_ENGINE = "django.contrib.sessions.backends.cached_db"
SESSION_COOKIE_DOMAIN = '.%s' % SITE_DOMAIN
SESSION_COOKIE_AGE = 60 * 60 * 24 * 90  # 90 days in seconds


## Bower settings

BOWER_COMPONENTS_ROOT = os.path.join(os.path.join(BASE_DIR, '..'), '..')
BOWER_INSTALLED_APPS = [
    'bootstrap',
    'jquery',
]


## Pipeline settings

PIPELINE = {
    'PIPELINE_ENABLED': True,
    'CSS_COMPRESSOR': 'localsite.compressors.rcssmin.RCSSMinCompressor',
    'JS_COMPRESSOR': 'localsite.compressors.rjsmin.RJSMinCompressor',
    'STYLESHEETS': {
        'common': {
            'source_filenames': (
                'bootstrap/dist/css/bootstrap.css',
                'css/custom.css',
            ),
            'output_filename': 'CACHE/common.min.css',
            'variant': 'datauri',
        },
    },
    'JAVASCRIPT': {
        'common': {
            'source_filenames': (
                'jquery/dist/jquery.js',
                'bootstrap/dist/js/bootstrap.js',
                'js/custom.js',
            ),
            'output_filename': 'CACHE/common.min.js',
            'extra_context': {
            },
        },
    }
}


## Robots settings

ROBOTS_USE_SITEMAP = False
ROBOTS_CACHE_TIMEOUT = 60 * 60 * 24
