from django.test import TestCase


class MarkupBaseTests(TestCase):
    """Tests the ``markupmirror.markup.base`` module basics."""

    def test_true(self):
        """Test"""
        self.assertTrue(True)


__all__ = ('MarkupBaseTests',)
