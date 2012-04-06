from django.test import TestCase

from markupmirror.markup.base import BaseMarkup


class MarkupBaseTests(TestCase):
    """Tests the ``markupmirror.markup.base`` module basics."""

    def test_name(self):
        """Tests ``BaseMarkup.get_name``."""

        self.assertEqual(BaseMarkup.get_name(), 'base')

        class DummyMarkup(BaseMarkup):
            pass

        self.assertEqual(DummyMarkup.get_name(), 'dummy')


__all__ = ('MarkupBaseTests',)
