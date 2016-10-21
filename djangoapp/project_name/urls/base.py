import re

from django.conf import settings
from django.conf.urls import include, url

urlpatterns = [
    url(settings.ADMIN_URL, include(admin.site.urls)),
    url(r'^robots\.txt$', include('robots.urls')),
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

urlpatterns += [
]
