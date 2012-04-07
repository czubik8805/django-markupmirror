from django.utils.encoding import smart_str

from markupmirror import settings
from markupmirror.markup.base import BaseMarkup
from markupmirror.markup.base import register_markup


class ReStructuredTextMarkup(BaseMarkup):
    """Markup transformer for reStructuredText content.

    """
    codemirror_mode = 'text/x-rst'

    def __init__(self):
        self.filter_settings = settings.RESTRUCTUREDTEXT_FILTER
        self.restructuredtext = publish_parts

    def convert(self, markup):
        parts = self.restructuredtext(
            source=smart_str(markup),
            writer_name='html4css1',
            settings_overrides=self.filter_settings)
        # Intentionally return ``html_body`` instead of ``fragment`` as
        # Django's templatetag does. ``html_body`` also includes the document's
        # title and subtitle, and if the first parts of ``markup`` are
        # headlines (=== or ---), they would be stripped off the result
        # otherwise.
        return parts['html_body']


# Only register if docutils is installed
try:
    from docutils.core import publish_parts
    register_markup(ReStructuredTextMarkup)
except ImportError:
    pass


__all__ = ('ReStructuredTextMarkup',)
