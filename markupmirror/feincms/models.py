from __future__ import absolute_import, unicode_literals

from django.db import models
from django.template.loader import render_to_string
from django.utils.translation import gettext_lazy as _

from markupmirror import settings
from markupmirror.fields import MarkupMirrorField


__all__ = ('MarkupMirrorContent',)


class MarkupMirrorContent(models.Model):
    """FeinCMS Page contenttype that stores markup in a MarkupMirrorField.

    """
    # TODO: find a way to include a button like richtext content
    # __name__ = 'richtextcontent'

    content = MarkupMirrorField(
        verbose_name=_("Markup content"),
        markup_type=settings.MARKUPMIRROR_DEFAULT_MARKUP_TYPE,
        blank=True,
    )

    class Meta:
        abstract = True
        app_label = 'wienfluss'
        verbose_name = _("Markup content")
        verbose_name_plural = _("Markup content")

    def render(self, **kwargs):
        request = kwargs.get('request')
        return render_to_string(
            template_name='content/markupmirror/default.html',
            context={
                'content': self,
                'request': request
            }
        )
