from __future__ import absolute_import, unicode_literals

from django.utils.html import linebreaks
from django.utils.html import urlize
from django.utils.translation import gettext_lazy as _

from markupmirror.markup.base import BaseMarkup


__all__ = ('PlainTextMarkup',)


class PlainTextMarkup(BaseMarkup):
    """Markup transformer for plain-text content.

    This uses Django's ``urlize`` and ``linebreaks`` utitlies to convert URLs
    in the text to clickable links and linebreaks to ``<p>`` and ``<br />``
    elements respectively.

    """
    codemirror_mode = 'text/plain'
    title = _("Plain text")

    def convert(self, markup, *args, **kwargs):
        return urlize(linebreaks(markup))
