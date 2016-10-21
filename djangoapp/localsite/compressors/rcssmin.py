from __future__ import absolute_import, unicode_literals

from pipeline.compressors import CompressorBase


class RCSSMinCompressor(CompressorBase):

    def compress_css(self, css):
        from rcssmin import cssmin
        return cssmin(css)
