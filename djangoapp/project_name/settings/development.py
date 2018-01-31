from .base import *

SECRET_KEY = 'sekrit'

DEBUG_PROPAGATE_EXCEPTIONS = True

INTERNAL_IPS = ['127.0.0.1', '0.0.0.0']

INSTALLED_APPS += [
    'template_timings_panel',
    'debug_toolbar',
]

if 'debug_toolbar' in INSTALLED_APPS:
    MIDDLEWARE_CLASSES += [
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    ]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '{{ project_name }}',
        'CONN_MAX_AGE': 600,
    }
}

ROOT_URLCONF = '{{ project_name }}.urls.development'

WSGI_APPLICATION = '{{ project_name }}.wsgi.development.application'


## Email / notification settings

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# Debug Toolbar settings

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': lambda request: True if DEBUG else False,
}
DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
    # Third-party panels...
    'template_timings_panel.panels.TemplateTimings.TemplateTimings',
]
if 'cachalot' in INSTALLED_APPS:
    DEBUG_TOOLBAR_PANELS += [
        'cachalot.panels.CachalotPanel',
    ]


## Cross Site Request Forgery protection

CSRF_COOKIE_DOMAIN = None


## Session settings

SESSION_COOKIE_DOMAIN = None


## Logging settings

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
        },
    },
    "loggers": {
        "django": {
            "level": "INFO",
            "handlers": ["console"],
        }
    }
}
