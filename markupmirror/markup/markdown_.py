from django.utils.translation import ugettext_lazy as _

from markupmirror import settings
from markupmirror.markup.base import BaseMarkup
from markupmirror.markup.base import register_markup


class MarkdownMarkup(BaseMarkup):
    """Markup transformer for `Markdown`_ content.

    .. _Markdown: http://daringfireball.net/projects/markdown/

    """
    codemirror_mode = 'text/x-markdown'
    title = _(u"Markdown")
    requires = ("markdown.Markdown", )

    def __init__(self):
        self.extensions = settings.MARKUPMIRROR_MARKDOWN_EXTENSIONS
        self.output_format = settings.MARKUPMIRROR_MARKDOWN_OUTPUT_FORMAT
        self.markdown = self.required['Markdown'](
            extensions=self.extensions,
            output_format=self.output_format)

    def convert(self, markup):
        return self.markdown.convert(markup)

__all__ = ('MarkdownMarkup',)
