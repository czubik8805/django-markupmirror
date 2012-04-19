.. _installation:

==============
 Installation
==============

The recommended way to install django-markupmirror is with `pip`_ (using
`easy_install`_ also works)::

    pip instal django-markupmirror

.. _pip: http://www.pip-installer.org/
.. _easy_install: http://peak.telecommunity.com/DevCenter/EasyInstall

Requirements
------------

django-markupmirror depends on:

* `Django`_ 1.4+ (for now tested with 1.4 only), obviously.

* `FeinCMS`_ 1.5+ (for now tested with 1.5.3 only), if you want to use the page
  content-type.

* `Markdown 2.1+`_, if you want to use the ``MarkdownMarkup`` converter.

* `Docutils 0.8+`_, if you want to use the ``ReStructuredTextMarkup``
  converter.

* `Textile 2.1+`_, if you want to use the ``TextileMarkup`` converter.

The three latter will be available automatically if the respective dependencies
are met.

.. _Django: http://pypi.python.org/pypi/Django
.. _FeinCMS: http://pypi.python.org/pypi/FeinCMS
.. _Markdown 2.1+: http://pypi.python.org/pypi/Markdown
.. _Docutils 0.8+: http://pypi.python.org/pypi/docutils
.. _Textile 2.1+: http://pypi.python.org/pypi/textile

Markup Types
------------

The markup-types available by default are:

``plaintext``
    Plain text markup. Converts URLs to links and linebreaks to breaks and
    paragraphs.

``html``
    Allows HTML. Therefore potentially unsafe.

``markdown``
    Converts `Markdown`_ to HTML.

``restructuredtext``
    Converts `reStructuredText`_ to HTML.

``textile``
    Converts `Textile`_ to HTML.

Settings & Configuration
------------------------

Use the configuration variables below in your ``settings.py`` to customize the
behaviour of django-markupmirror:

.. py:data:: MARKUPMIRROR_DEFAULT_MARKUP_TYPE

   Defines any of the above markup-types as default for fields where no
   ``markup_type`` or ``default_markup_type`` has been set explicitly.

   Defaults to ``plaintext``.

.. py:data:: MARKUPMIRROR_MARKDOWN_EXTENSIONS

   Defines the extensions to load for `Markdown`_. Markdown's package
   documentation contains `a list of available extensions`_.

   Defaults to ``['extra', 'headerid(level=2)']``.

.. py:data:: MARKUPMIRROR_MARKDOWN_OUTPUT_FORMAT

   Defines the output format for Markdown. One of ``HTML4``, ``XHTML`` and
   ``HTML5``.

   Defaults to ``HTML5``.

.. py:data:: MARKUPMIRROR_TEXTILE_SETTINGS

   Dictionary of arguments passed directly to the Textile converter defined in
   ``textile.functions.textile``.

   The converter's default function signature is:
   ``head_offset=0, html_type='xhtml', auto_link=False, encoding=None,
   output=None``.

   Defaults to: ``{'encoding': 'utf-8', 'output': 'utf-8'}``

.. py:data:: MARKUPMIRROR_FEINCMS_INIT_TEMPLATE

   Defines the template used by FeinCMS to initialize Pages with
   ``MarkupMirrorContent`` blocks.

   .. deprecated:: 0.1a2
      This will soon be obsolete due to a generic jQuery plugin to initialize
      the CodeMirror editor anywhere.

.. py:data:: MARKUPMIRROR_FEINCMS_INIT_CONTEXT

   Context passed to the ``MARKUPMIRROR_FEINCMS_INIT_TEMPLATE``.

   .. deprecated:: 0.1a2
      This will soon be obsolete due to a generic jQuery plugin to initialize
      the CodeMirror editor anywhere.

.. _Markdown: http://daringfireball.net/projects/markdown/
.. _reStructuredText: http://docutils.sourceforge.net/rst.html
.. _Textile: http://www.textism.com/tools/textile/
.. _Markdown's package documentation: http://packages.python.org/Markdown/
.. _a list of available extensions:
    http://packages.python.org/Markdown/extensions/
