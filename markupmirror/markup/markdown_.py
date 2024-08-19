from __future__ import absolute_import, unicode_literals

from django.utils.translation import gettext_lazy as _

from markupmirror import settings
from markupmirror.markup.base import BaseMarkup


__all__ = ('MarkdownMarkup',)


class MarkdownMarkup(BaseMarkup):
    """Markup transformer for `Markdown`_ content.

    .. _Markdown: http://daringfireball.net/projects/markdown/

    """
    codemirror_mode = 'text/x-markdown'
    title = _("Markdown")
    requires = {
        'markdown': 'markdown.Markdown',
    }

    def __init__(self):
        self.extensions = settings.MARKUPMIRROR_MARKDOWN_EXTENSIONS
        self.output_format = settings.MARKUPMIRROR_MARKDOWN_OUTPUT_FORMAT
        self.markdown = self.requirements['markdown'](
            extensions=self.extensions,
            output_format=self.output_format)

    def convert(self, markup, *args, **kwargs):
        return self.markdown.convert(markup)
