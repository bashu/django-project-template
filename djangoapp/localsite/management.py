# -*- coding: utf-8

import socket

from django.conf import settings
from django.apps import apps as global_apps
from django.core.management.color import no_style
from django.db import DEFAULT_DB_ALIAS, connections, router


def create_default_site(app_config, verbosity=2, interactive=True, using=DEFAULT_DB_ALIAS, apps=global_apps, **kwargs):
    try:
        Site = apps.get_model('sites', 'Site')
    except LookupError:
        return

    if not router.allow_migrate_model(using, Site):
        return

    from django.contrib.sites import management

    if not Site.objects.using(using).exists():
        management.create_default_site(app_config=app_config, verbosity=verbosity)

    site = Site.objects.get(pk=getattr(settings, "SITE_ID", 1))
    site.name, site.domain = (
        getattr(settings, "SITE_NAME", 'example.com'), getattr(settings, "SITE_DOMAIN", socket.gethostname()),
    )
    site.save(using=using)
    
    Site.objects.clear_cache()
