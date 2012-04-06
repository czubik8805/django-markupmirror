from markupmirror import settings
from markupmirror.markup.base import BaseMarkup
from markupmirror.markup.base import register_markup


class TextileMarkup(BaseMarkup):
    """Markup transformer for Textile content.

    """
    def __init__(self):
        self.textile_settings = settings.TEXTILE_SETTINGS
        self.textile = textile

    def convert(self, markup):
        return self.textile(markup, **self.textile_settings)


# Only register if textile is installed
try:
    from textile import textile
    register_markup(TextileMarkup)
except ImportError:
    pass


__all__ = ('TextileMarkup',)