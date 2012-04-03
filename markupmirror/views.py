from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib.markup.templatetags.markup import markdown
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.generic.base import View

from markdownmirror.settings import MARKDOWN_EXTENSIONS


class MarkupPreview(View):
    """Renders markup content to HTML for preview purposes."""

    http_method_names = ['post']

    @method_decorator(login_required)
    @method_decorator(user_passes_test(lambda user: user.is_staff))
    def post(self, request, *args, **kwargs):
        text = self.request.POST.get('text', u"")
        return HttpResponse(
            unicode(markdown(text, MARKDOWN_EXTENSIONS)),
            content_type='text/html')


__all__ = ('MarkupMirrorPreview',)
