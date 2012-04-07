from django import forms
from django.utils.translation import ugettext_lazy as _

from feincms.admin.item_editor import ItemEditorForm

from markupmirror.markup.base import markup_pool


class MarkupMirrorContentAdminForm(ItemEditorForm):
    """Custom admin form for MarkupMirrorContent in FeinCMS pages.

    This initializes the CodeMirror editor and preview for each text area.

    """
    content = forms.CharField(
        widget=forms.Textarea,
        required=False,
        label=_(u"text"))

    def __init__(self, *args, **kwargs):
        super(MarkupMirrorContentAdminForm, self).__init__(*args, **kwargs)

        # add 'item-markupmirror' class and mode for CodeMirror
        markup_type = self.fields['content'].default_markup_type
        markup = markup_pool.get_markup(markup_type)
        self.fields['content'].widget.attrs.update({
            'class': 'item-markupmirror',
            'data-mode': markup.codemirror_mode,
        })


__all__ = ('MarkupMirrorContentAdminForm',)
