from __future__ import absolute_import, unicode_literals

from django.conf.urls import include, url

from markupmirror import urls as markupmirror_urls


urlpatterns = [
    url(r'^markupmirror/', include(markupmirror_urls)),
]
