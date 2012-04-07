from django.db import models
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _


from markupmirror import settings
from markupmirror.feincms.admin import MarkupMirrorContentAdminForm
from markupmirror.fields import MarkupMirrorField


class MarkupMirrorContent(models.Model):
    """FeinCMS Page contenttype that stores markup in a MarkupMirrorField.

    """
    # TODO: find a way to include a button like richtext content
    # __name__ = 'richtextcontent'

    form = MarkupMirrorContentAdminForm
    feincms_item_editor_form = MarkupMirrorContentAdminForm
    feincms_item_editor_context_processors = (
        lambda x: settings.FEINCMS_MARKUPMIRRORCONTENT_INIT_CONTEXT,
    )
    feincms_item_editor_includes = {
        'head': [settings.FEINCMS_MARKUPMIRRORCONTENT_INIT_TEMPLATE],
    }

    content = MarkupMirrorField(
        verbose_name=_(u"Markdown content"), markup_type='markdown',
        blank=True)

    class Meta:
        abstract = True
        app_label = 'wienfluss'
        verbose_name = _('Markdown content')
        verbose_name_plural = _('Markdown content')

    def render(self, **kwargs):
        request = kwargs.get('request')
        return render_to_string('content/markdown/default.html', {
            'content': self,
            'request': request
        })


__all__ = ('MarkDownContent',)
