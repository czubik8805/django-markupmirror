from django.conf.urls import patterns
from django.conf.urls import url
from django.views.generic.base import TemplateView

from markupmirror.views import MarkupPreview


urlpatterns = patterns('',
    url(r'^preview/(?P<markup_type>[\w-]+)/$',
        MarkupPreview.as_view(),
        name='preview'),
    url(r'^base/$',
        TemplateView.as_view(
            template_name='markupmirror/preview.html'),
        name='base'),
)
