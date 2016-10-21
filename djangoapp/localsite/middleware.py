# -*- coding: utf-8 -*-


class RemoteAddrMiddleware(object):

    def process_request(self, request):
        if 'HTTP_X_FORWARDED_FOR' in request.META:
            ipaddr = request.META['HTTP_X_FORWARDED_FOR'].split(",")[0].strip()
            request.META['REMOTE_ADDR'] = ipaddr

        # fallback...
        if not 'REMOTE_ADDR' in request.META:
            try:
                request.META['REMOTE_ADDR'] = request.META['HTTP_X_REAL_IP']
            except KeyError:
                # This will place a valid IP in REMOTE_ADDR but this
                # shouldn't happen
                request.META['REMOTE_ADDR'] = '127.0.0.1'

        if 'unknown' in request.META['REMOTE_ADDR']:
            request.META['REMOTE_ADDR'] = '127.0.0.1'
