from django.conf import settings


MARKUPMIRROR_DEFAULT_MARKUP_TYPE = getattr(settings,
    'MARKUPMIRROR_DEFAULT_MARKUP_TYPE', 'plaintext')
"""Defines any of the :ref:`default markup-types <usage-markup-types-default>`
as default for fields where no ``markup_type`` or ``default_markup_type``
has been set explicitly.

Defaults to ``plaintext``.

"""

# CodeMirror settings

# Minified JS and CSS files
MARKUPMIRROR_JS = (
    'markupmirror/jquery-1.7.2.min.js',
    'markupmirror/codemirror.min.js',
    'markupmirror/markupmirror.js',
)
MARKUPMIRROR_CSS = (
    'markupmirror/codemirror.min.css',
    'markupmirror/markupmirror.css',
)


# Settings for markup converters

# Extensions and settings for markdown
MARKUPMIRROR_MARKDOWN_EXTENSIONS = getattr(settings,
    'MARKUPMIRROR_MARKDOWN_EXTENSIONS',
    ['extra', 'headerid(level=2)'])
"""Defines the extensions to load for `Markdown`_. `Markdown's package
documentation`_ contains `a list of available extensions`_.

Defaults to ``['extra', 'headerid(level=2)']``.

.. _Markdown: http://daringfireball.net/projects/markdown/
.. _Markdown's package documentation: http://packages.python.org/Markdown/
.. _a list of available extensions:
    http://packages.python.org/Markdown/extensions/

"""
MARKUPMIRROR_MARKDOWN_OUTPUT_FORMAT = getattr(settings,
    'MARKUPMIRROR_MARKDOWN_OUTPUT_FORMAT',
    'html5')
"""Defines the output format for Markdown. One of ``HTML4``, ``XHTML`` and
``HTML5``.

Defaults to ``HTML5``.

"""

# Textile settings
MARKUPMIRROR_TEXTILE_SETTINGS = getattr(settings,
    'MARKUPMIRROR_TEXTILE_SETTINGS',
    {'encoding': 'utf-8', 'output': 'utf-8'})
"""Dictionary of arguments passed directly to the Textile converter defined in
``textile.functions.textile``.

The converter's default function signature is:
``head_offset=0, html_type='xhtml', auto_link=False, encoding=None,
output=None``.

Defaults to: ``{'encoding': 'utf-8', 'output': 'utf-8'}``

"""


# Settings for MarkupMirrorContent for FeinCMS

# Init template for CodeMirror in FeinCMS
MARKUPMIRROR_FEINCMS_INIT_TEMPLATE = getattr(settings,
    'MARKUPMIRROR_FEINCMS_INIT_TEMPLATE',
    'admin/markupmirror/feincms/init_codemirror.html')
"""Defines the template used by FeinCMS to initialize Pages with
``MarkupMirrorContent`` blocks.

.. deprecated:: 0.1a2
   This will soon be obsolete due to a generic jQuery plugin to initialize
   the CodeMirror editor anywhere.

"""
# Context for init template
MARKUPMIRROR_FEINCMS_INIT_CONTEXT = getattr(settings,
    'MARKUPMIRROR_FEINCMS_INIT_CONTEXT', {
    #     'CODEMIRROR_JS': CODEMIRROR_JS,
    #     'CODEMIRROR_CSS': CODEMIRROR_CSS,
        'CODEMIRROR_PATH': settings.STATIC_URL + 'markupmirror/',
        'CODEMIRROR_WIDTH': '50%',
        'CODEMIRROR_HEIGHT': '300px',
    })
"""Context passed to the ``MARKUPMIRROR_FEINCMS_INIT_TEMPLATE``.

.. deprecated:: 0.1a2
   This will soon be obsolete due to a generic jQuery plugin to initialize
   the CodeMirror editor anywhere.

"""
