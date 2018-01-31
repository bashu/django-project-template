# -*- coding: utf-8 -*-

from django.conf import settings

from pipeline.storage import PipelineMixin
from storages.backends.s3boto import S3BotoStorage
from whitenoise.django import GzipManifestStaticFilesStorage


class FixedS3BotoMixin(object):

    # HACK: Fixing handling of folder names.
    def url(self, name, *args, **kwargs):
        url = super(FixedS3BotoMixin, self).url(name, *args, **kwargs)
        if name.endswith('/') and not url.endswith('/'):
            url += '/'
        return url


class DefaultStorage(FixedS3BotoMixin, S3BotoStorage):
    location = settings.MEDIAFILES_LOCATION


class GzipManifestPipelineStorage(PipelineMixin, GzipManifestStaticFilesStorage):
    pass
