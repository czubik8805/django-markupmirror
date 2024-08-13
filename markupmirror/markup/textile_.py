from __future__ import absolute_import, unicode_literals

from django.utils.translation import gettext_lazy as _

from markupmirror import settings
from markupmirror.markup.base import BaseMarkup


__all__ = ('TextileMarkup',)


class TextileMarkup(BaseMarkup):
    """Markup transformer for `Textile`_ content.

    .. _Textile: http://www.textism.com/tools/textile/

    """
    codemirror_mode = 'text/plain'
    title = _("Textile")
    requires = {
        'textile': 'textile.textile',
    }

    def __init__(self):
        self.textile_settings = settings.MARKUPMIRROR_TEXTILE_SETTINGS
        self.textile = self.requirements['textile']

    def convert(self, markup, *args, **kwargs):
        return self.textile(markup, **self.textile_settings)
