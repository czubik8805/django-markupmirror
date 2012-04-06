from django.test import TestCase

from markupmirror.exceptions import InvalidMarkup
from markupmirror.exceptions import MarkupAlreadyRegistered
from markupmirror.exceptions import MarkupNotFound
from markupmirror.markup.base import BaseMarkup
from markupmirror.markup.base import markup_pool
from markupmirror.markup.base import register_markup


class DummyMarkup(BaseMarkup):
    pass


class BaseMarkupTests(TestCase):
    """Tests the ``markupmirror.markup.base.BaseMarkup`` class that acts as
    a base class for markup converters.

    """
    def test_name(self):
        """Tests ``BaseMarkup.get_name``."""

        self.assertEqual(BaseMarkup.get_name(), 'base')
        self.assertEqual(DummyMarkup.get_name(), 'dummy')

    def test_convert_markup(self):
        """Tests that the order of the three convert methods
        ``before_convert``, ``convert`` and ``after_convert`` is kept
        correctly.

        """
        class DummyMarkup(BaseMarkup):

            def before_convert(self, markup):
                return markup.replace("1", "2", 1)

            def convert(self, markup):
                return markup.replace("2", "3", 1)

            def after_convert(self, markup):
                return markup.replace("3", "4", 1)

        dummy_markup = DummyMarkup()

        self.assertEqual(dummy_markup.before_convert("1"), "2")
        self.assertEqual(dummy_markup.convert("2"), "3")
        self.assertEqual(dummy_markup.after_convert("3"), "4")
        # test order
        self.assertEqual(dummy_markup("1"), "4")

    def test_base_convert(self):
        """The ``BaseMarkup`` converter does not do anything."""
        bm = BaseMarkup()
        self.assertEqual(bm.before_convert("markup"), "markup")
        self.assertEqual(bm.convert("markup"), "markup")
        self.assertEqual(bm.after_convert("markup"), "markup")


class MarkupPoolTests(TestCase):
    """Tests the ``markupmirror.markup.base.MarkupPool``."""

    def tearDown(self):
        markup_pool.unregister_markup('dummy')

    def test_register_invalid(self):
        """Registering a markup class which does not subclass ``BaseMarkup``
        raises an ``InvalidMarkup`` exception.

        """
        class InvalidMarkupClass(object):
            pass

        self.assertRaises(InvalidMarkup, register_markup, InvalidMarkupClass)

    def test_re_register(self):
        """Registering a markup converter twice raises a
        ``MarkupAlreadyRegistered`` exception.

        """
        register_markup(DummyMarkup)
        self.assertRaises(MarkupAlreadyRegistered,
                          register_markup, DummyMarkup)

    def test_register(self):
        """Registering a markup converter makes it available through its name.

        """
        # before the markup is registered, we'll get ``MarkupNotFound`` if
        # we try to retrieve it.
        self.assertRaises(MarkupNotFound, markup_pool.get_markup, 'dummy')

        # it is available after registering it
        register_markup(DummyMarkup)
        self.assertTrue(
            isinstance(markup_pool.get_markup('dummy'), DummyMarkup))

    def test_unregister(self):
        """Unregistering a markup converter removes it from the pool."""
        register_markup(DummyMarkup)
        self.assertTrue(
            isinstance(markup_pool.get_markup('dummy'), DummyMarkup))
        markup_pool.unregister_markup('dummy')
        self.assertRaises(MarkupNotFound, markup_pool.get_markup, 'dummy')

    def test_get_all(self):
        """``markup_pool.get_all_markups`` returns all markup converters
        sorted by name.

        """
        all_markups = markup_pool.get_all_markups()
        self.assertEqual(
            sorted([markup.get_name() for markup in all_markups]),
            ['html', 'markdown', 'plaintext', 'restructuredtext', 'textile'])


__all__ = ('BaseMarkupTests', 'MarkupPoolTests')
