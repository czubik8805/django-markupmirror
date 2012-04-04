from django.conf.urls.defaults import include
from django.conf.urls.defaults import patterns

urlpatterns = patterns('',
    (r'^markupmirror/', include('markupmirror.urls')),
)
