from __future__ import absolute_import, unicode_literals

from pipeline.compressors import CompressorBase


class RJSMinCompressor(CompressorBase):

    def compress_js(self, js):
        from rjsmin import jsmin
        return jsmin(js)
