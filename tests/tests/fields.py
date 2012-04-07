from django.test import TestCase

from markupmirror.fields import Markup
from markupmirror.fields import MarkupMirrorField
from markupmirror.fields import MarkupMirrorFieldDescriptor
from markupmirror.widgets import MarkupMirrorTextarea
from markupmirror.widgets import AdminMarkupMirrorTextareaWidget

from tests.tests.models import Post, Article, Abstract, Concrete


class MarkupMirrorFieldTests(TestCase):
    """Tests the ``markupmirror.fields.MarkupMirrorField`` implementation."""

    def setUp(self):
        self.mp = Post(title='example markdown post',
                       body='**markdown**',
                       body_markup_type='markdown')

    def test_verbose_name(self):
        self.assertEqual(self.mp._meta.get_field('body').verbose_name,
                         'post body')