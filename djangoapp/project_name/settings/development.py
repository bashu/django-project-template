from .base import *

DEBUG_PROPAGATE_EXCEPTIONS = True

INTERNAL_IPS = ['127.0.0.1', '0.0.0.0']

INSTALLED_APPS += [
    'template_timings_panel',
    'debug_toolbar',
]

MIDDLEWARE_CLASSES += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = '{{ project_name }}.urls.development'

WSGI_APPLICATION = '{{ project_name }}.wsgi.development.application'


## Email / notification settings

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# Debug Toolbar settings

DEBUG_TOOLBAR_PATCH_SETTINGS = False
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
CSRF_COOKIE_DOMAIN = None
SESSION_COOKIE_DOMAIN = None
