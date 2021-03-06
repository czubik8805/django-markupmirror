from __future__ import absolute_import, unicode_literals
import textwrap

from django.test import TestCase

from markupmirror.markup.markdown_ import MarkdownMarkup


__all__ = ('MarkdownMarkupTests',)


MARKUP = """\
A First Level Header
====================

A Second Level Header
---------------------

Now is the time for all good men to come to
the aid of their country. This is just a
regular paragraph.

The quick brown fox jumped over the lazy
dog's back.

### Header 3

> This is a blockquote.
>
> This is the second paragraph in the blockquote.
>
> ## This is an H2 in a blockquote
"""


class MarkdownMarkupTests(TestCase):
    """Tests the ``markupmirror.markup.markdown_.MarkdownMarkup`` class that
    converts Markdown content to HTML.

    """
    def test_convert(self):
        """The ``MarkdownMarkup`` converter uses python-markdown to convert
        markdown to HTML.

        """
        markdown_markup = MarkdownMarkup()
        self.assertHTMLEqual(
            markdown_markup(MARKUP),
            textwrap.dedent("""\
                <h1>A First Level Header</h1>
                <h2>A Second Level Header</h2>
                <p>Now is the time for all good men to come to
                    the aid of their country. This is just a
                    regular paragraph.</p>
                <p>The quick brown fox jumped over the lazy dog's back.</p>
                <h3>Header 3</h3>
                <blockquote>
                    <p>This is a blockquote.</p>
                    <p>This is the second paragraph in the blockquote.</p>
                    <h2>This is an H2 in a blockquote</h2>
                </blockquote>
                """))

    # TODO: don't know how to fake an ImportError.
    #       Excluded in tests.settings.COVERAGE_CODE_EXCLUDES.
    #
    # def test_no_markdown(self):
    #     """If markdown is not installed, the converter will just not be
    #     available.

    #     """
    #     # first, remove already registered markdown converter
    #     markup_pool.unregister_markup('markdown')
    #     self.assertRaises(KeyError, markup_pool.get_markup, 'markdown')

    #     # trying to import markdown fails
    #     with self.assertRaises(ImportError):
    #         from markdown import Markdown

    #     # now try to re-register by importing markdown_ module
    #     # this tries to import markdown and fails silently
    #     from markupmirror.markup import markdown_

    #     # markdown should not be found
    #     self.assertRaises(KeyError, markup_pool.get_markup, 'markdown')

    #     # re-register markdown to restore default state
    #     register_markup(MarkdownMarkup)
