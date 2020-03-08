from functools import wraps

import json
import urllib

from django.conf import settings
from django.contrib import messages


def check_recaptcha(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        request.recaptcha_is_valid = None
        if request.method == 'POST':
            captcha_response = request.POST.get('g-recaptcha-response')
            values = {
                'secret': settings.HCAPTCHA_SECRET_KEY,
                'response': captcha_response,
                'remoteip': request.META.get("REMOTE_ADDR"),
            }

            data = urllib.parse.urlencode(values).encode()
            req = urllib.request.Request(settings.CAPTCHA_VERIFY_LINK, data=data)
            response = urllib.request.urlopen(req)
            result = json.loads(response.read().decode())

            if result['success']:
                request.recaptcha_is_valid = True
            else:
                request.recaptcha_is_valid = False
                messages.error(request, 'Invalid reCAPTCHA. Please try again.')
        return view_func(request, *args, **kwargs)
    return _wrapped_view
