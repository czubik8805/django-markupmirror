from __future__ import absolute_import, unicode_literals

from django.conf.urls import include

import django
from packaging.version import parse


django_version = parse(django.get_version())

if django_version < parse('4.0'):
    from django.conf.urls import url
else:
    from django.urls import re_path as url


from markupmirror import urls as markupmirror_urls


urlpatterns = [
    url(r'^markupmirror/', include(markupmirror_urls)),
]
