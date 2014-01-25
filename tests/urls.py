from __future__ import absolute_import, unicode_literals

from django.conf.urls.defaults import include, patterns

import markupmirror.urls


urlpatterns = patterns(
    '',
    (r'^markupmirror/', include(markupmirror.urls.preview)),
)
