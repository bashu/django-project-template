"""{{ project_name }} URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/{{ docs_version }}/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import re

from django.conf import settings
from django.conf.urls import include, url

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
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
