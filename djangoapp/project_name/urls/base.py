import re

from django.conf import settings
from django.conf.urls import include, url

from django.contrib import admin

urlpatterns = [
    url(settings.ADMIN_URL, include(admin.site.urls)),
]

if settings.DEBUG and 'debug_toolbar' in settings.INSTALLED_APPS:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]

if settings.SERVE_MEDIA:
    from django.views.static import serve
    urlpatterns += [
        url(r'^%s(?P<path>.*)$' % re.escape(settings.STATIC_URL.lstrip('/')), serve, kwargs={
            'document_root': settings.STATIC_ROOT,
        }),
    ]

    urlpatterns += [
        url(r'^%s(?P<path>.*)$' % re.escape(settings.MEDIA_URL.lstrip('/')), serve, kwargs={
            'document_root': settings.MEDIA_ROOT,
        }),
    ]

if 'robots' in settings.INSTALLED_APPS:
    urlpatterns += [
        url(r'^robots\.txt', include('robots.urls')),
]

if 'localsite' in settings.INSTALLED_APPS:
    urlpatterns += [
        url(r'^', include('localsite.urls')),    
    ]
