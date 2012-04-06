from markupmirror import settings
from markupmirror.markup.base import BaseMarkup
from markupmirror.markup.base import register_markup


class ReStructuredTextMarkup(BaseMarkup):
    """Markup transformer for reStructuredText content.

    """
    def __init__(self):
        self.filter_settings = settings.RESTRUCTUREDTEXT_FILTER
        self.restructuredtext = publish_parts

    def __call__(self, markup):
        parts = self.restructuredtext(
            source=markup,
            writer_name='html4css1',
            settings_overrides=self.filter_settings)
        return parts['fragment']


# Only register if docutils is installed
try:
    from docutils.core import publish_parts
    register_markup(ReStructuredTextMarkup)
except ImportError:
    pass


__all__ = ('ReStructuredTextMarkup',)
