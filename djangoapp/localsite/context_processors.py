# -*- coding: utf-8 -*-

from template_utils.context_processors import settings_processor

localsite_settings = settings_processor(
    'SITE_NAME', 'SITE_DOMAIN', 'CONTACT_EMAIL',
)
