from django.utils.html import linebreaks
from django.utils.html import urlize

from markupmirror.markup.base import BaseMarkup
from markupmirror.markup.base import register_markup


class PlainTextMarkup(BaseMarkup):
    """Markup transformer for plain-text content.

    This uses Django's ``urlize`` and ``linebreaks`` utitlies to convert URLs
    in the text to clickable links and linebreaks to ``<p>`` and ``<br />``
    elements respectively.

    """
    def __call__(self, markup):
        return urlize(linebreaks(markup))


register_markup(PlainTextMarkup)


__all__ = ('PlainTextMarkup',)
