from django.conf.urls import patterns
from django.conf.urls import url
from django.views.generic.base import TemplateView

from wienfluss.models.pagecontent.markdown.models import MarkDownContentPreview


urlpatterns = patterns('',
    url(r'^preview/$',
        MarkDownContentPreview.as_view(),
        name='preview'),
    url(r'^base/$',
        TemplateView.as_view(
            template_name='markupmirror/preview.html'),
        name='base'),
)
