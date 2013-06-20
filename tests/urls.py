from __future__ import absolute_import, unicode_literals

from django.conf.urls.defaults import include

import markupmirror.urls


urlpatterns = [
    (r'^markupmirror/', include(markupmirror.urls.preview)),
]
