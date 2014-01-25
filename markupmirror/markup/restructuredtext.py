from __future__ import absolute_import, unicode_literals

try:
    from django.utils.encoding import smart_bytes
except ImportError:
    from django.utils.encoding import smart_str as smart_bytes

from django.utils.translation import ugettext_lazy as _

from markupmirror.markup.base import BaseMarkup


__all__ = ('ReStructuredTextMarkup',)


class ReStructuredTextMarkup(BaseMarkup):
    """Markup transformer for `reStructuredText`_ content.

    .. _reStructuredText: http://docutils.sourceforge.net/rst.html

    """
    codemirror_mode = 'text/x-rst'
    title = _("reStructuredText")
    requires = {
        'rest': 'docutils.core.publish_parts',
    }

    def __init__(self):
        self.restructuredtext = self.requirements['rest']

    def convert(self, markup, *args, **kwargs):
        parts = self.restructuredtext(
            source=smart_bytes(markup),
            writer_name='html4css1')
        # Intentionally return ``html_body`` instead of ``fragment`` as
        # Django's templatetag does. ``html_body`` also includes the document's
        # title and subtitle, and if the first parts of ``markup`` are
        # headlines (=== or ---), they would be stripped off the result
        # otherwise.
        return parts['html_body']
