# -*- coding: utf-8 -*-

import importlib

from django.conf import settings
from django.db.models.signals import post_migrate
from django.apps import AppConfig as DefaultAppConfig


class AppConfig(DefaultAppConfig):
    name = 'localsite'

    def ready(self):
        # Ensure everything below is only ever run once
        if getattr(AppConfig, 'has_run_ready', False):
            return
        AppConfig.has_run_ready = True

        if 'django.contrib.sites' in settings.INSTALLED_APPS:
            from .management import create_default_site

            post_migrate.connect(create_default_site, sender=self)

        try:
            importlib.import_module('localsite.receivers')
        except ImportError:
            pass
