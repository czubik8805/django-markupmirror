from django.utils.encoding import smart_str
from django.utils.translation import ugettext_lazy as _

from markupmirror.markup.base import BaseMarkup
from markupmirror.markup.base import register_markup


class ReStructuredTextMarkup(BaseMarkup):
    """Markup transformer for `reStructuredText`_ content.

    .. _reStructuredText: http://docutils.sourceforge.net/rst.html

    """
    codemirror_mode = 'text/x-rst'
    title = _(u"reStructuredText")
    requires = ('docutils.core.publish_parts', )

    def __init__(self):
        self.restructuredtext = self.required['publish_parts']

    def convert(self, markup):
        parts = self.restructuredtext(
            source=smart_str(markup),
            writer_name='html4css1')
        # Intentionally return ``html_body`` instead of ``fragment`` as
        # Django's templatetag does. ``html_body`` also includes the document's
        # title and subtitle, and if the first parts of ``markup`` are
        # headlines (=== or ---), they would be stripped off the result
        # otherwise.
        return parts['html_body']

__all__ = ('ReStructuredTextMarkup',)
