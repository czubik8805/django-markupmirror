from django import forms
from django.contrib.admin.widgets import AdminTextareaWidget

from markupmirror import settings
from markupmirror.markup.base import markup_pool


class MarkupMirrorTextarea(forms.Textarea):

    def render(self, name, value, attrs=None):
        if value is not None and not isinstance(value, unicode):
            value = value.raw
        return super(MarkupMirrorTextarea, self).render(name, value, attrs)

    class Media:
        css = {
            'all': settings.MARKUPMIRROR_CSS
        }
        js = settings.MARKUPMIRROR_JS


class AdminMarkupMirrorTextareaWidget(
    MarkupMirrorTextarea, AdminTextareaWidget):

    def render(self, name, value, attrs=None):
        """Adds attributes necessary to load CodeMirror for each textarea
        in the admin.

        """
        if value and hasattr(value, 'markup_type'):
            # get markup converter by type.
            # ``value`` is ``markupmirror.fields.Markup``.
            markup_type = value.markup_type
            markup = markup_pool.get_markup(markup_type)

            default_attrs = {
                'data-mode': markup.codemirror_mode,
                'data-markuptype': markup_type,
            }
            default_attrs.update(attrs)

        return super(AdminMarkupMirrorTextareaWidget, self).render(
            name, value, attrs)


__all__ = ('MarkupMirrorTextarea', 'AdminMarkupMirrorTextareaWidget')
