# -*- coding: utf-8 -*-

import os

from django.conf import settings

from pipeline.storage import PipelineMixin
from storages.backends.s3boto import S3BotoStorage
from whitenoise.django import GzipManifestStaticFilesStorage

os.environ['S3_USE_SIGV4'] = 'True'


class FixedS3BotoMixin(object):

    # HACK: Fixing handling of folder names.
    def url(self, name, *args, **kwargs):
        url = super(FixedS3BotoMixin, self).url(name, *args, **kwargs)
        if name.endswith('/') and not url.endswith('/'):
            url += '/'
        return url


class DefaultStorage(FixedS3BotoMixin, S3BotoStorage):

    def __init__(self, *args, **kwargs):
        kwargs['location'] = settings.MEDIA_ROOT
        super(DefaultStorage, self).__init__(*args, **kwargs)

    @property
    def connection(self):
        if self._connection is None:
            self._connection = self.connection_class(
                self.access_key, self.secret_key,
                calling_format=self.calling_format, host='s3.eu-central-1.amazonaws.com')
        return self._connection


class GzipManifestPipelineStorage(PipelineMixin, GzipManifestStaticFilesStorage):
    pass
