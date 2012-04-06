import textwrap

from django.test import TestCase

from markupmirror.markup.plaintext import PlainTextMarkup


class PlainTextMarkupTests(TestCase):
    """Tests the ``markupmirror.markup.plaintext.PlainTextMarkup`` class that
    does simple conversion of linebreaks and URLs.

    """
    def setUp(self):
        self.markup = textwrap.dedent(u"""\
            This is some plaintext markup.
            It includes http://www.domain.com/ links and

            also some linebreaks.
            """)

    def test_convert(self):
        plaintext_markup = PlainTextMarkup()
        self.assertHTMLEqual(
            plaintext_markup(self.markup),
            textwrap.dedent(u"""\
                <p>This is some plaintext markup.<br />
                It includes <a href="http://www.domain.com/">
                    http://www.domain.com/</a> links and</p>
                <p>also some linebreaks.<br /></p>
                """))


__all__ = ('PlainTextMarkupTests',)
