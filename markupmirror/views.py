from __future__ import absolute_import, unicode_literals

from django.http import HttpResponse
from django.views.generic.base import View

from markupmirror.markup.base import markup_pool


__all__ = ('MarkupMirrorPreview',)


class MarkupPreview(View):
    """Renders markup content to HTML for preview purposes."""

    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        markup_type = self.request.POST.get('markup_type')
        if not markup_type:
            return HttpResponse("", content_type='text/html')
        markup = markup_pool.get_markup(markup_type)
        text = self.request.POST.get('text', "")
        converted = markup(text, request=request)
        return HttpResponse(converted, content_type='text/html')
