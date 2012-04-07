from django import forms
from django.contrib.admin.widgets import AdminTextareaWidget


class MarkupMirrorTextarea(forms.Textarea):

    def render(self, name, value, attrs=None):
        if value is not None and not isinstance(value, unicode):
            value = value.raw
        return super(MarkupMirrorTextarea, self).render(name, value, attrs)


class AdminMarkupMirrorTextareaWidget(
    MarkupMirrorTextarea, AdminTextareaWidget):
    pass


__all__ = ('MarkupMirrorTextarea', 'AdminMarkupMirrorTextareaWidget')
