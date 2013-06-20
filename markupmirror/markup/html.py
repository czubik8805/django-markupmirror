from __future__ import absolute_import, unicode_literals

from django.utils.translation import ugettext_lazy as _

from markupmirror.markup.base import BaseMarkup


__all__ = ('HtmlMarkup',)


class HtmlMarkup(BaseMarkup):
    """Markup pseudo-transformer for HTML content.

    This does not transform anything and thus is potentially harmful.
    Use with care.

    """
    codemirror_mode = 'text/html'
    title = _("HTML")
