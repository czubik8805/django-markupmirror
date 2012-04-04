from markupmirror import settings
from markupmirror.markup.base import BaseMarkup
from markupmirror.markup.base import register_markup


class MarkdownMarkup(BaseMarkup):
    """Markup transformer for Markdown content.

    """
    def __init__(self):
        self.extensions = settings.MARKDOWN_EXTENSIONS
        self.markdown = markdown

    def __call__(self, markup):
        return self.markdown(markup, extensions=self.extensions)


# Only register if Markdown is installed
try:
    from markdown import markdown
    register_markup(MarkdownMarkup)
except ImportError:
    pass


__all__ = ('MarkdownMarkup',)
