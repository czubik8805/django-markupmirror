from django.conf import settings


# CodeMirror settings

# Separate modules of CodeMirror
CODEMIRROR_PATH = settings.STATIC_URL + 'markupmirror/codemirror/'
# Minified JS and CSS files
CODEMIRROR_JS = (
    CODEMIRROR_PATH + 'codemirror.min.js',
)
CODEMIRROR_CSS = (
    CODEMIRROR_PATH + 'codemirror.min.css',
    settings.STATIC_URL + 'markupmirror/css/markupmirror.css',
)


# Settings for markup converters

# Extensions and settings for markdown
MARKDOWN_EXTENSIONS = getattr(settings,
    'MARKUPMIRROR_MARKDOWN_EXTENSIONS',
    ['extra', 'headerid(level=2)', 'sane_lists'])
MARKDOWN_OUTPUT_FORMAT = getattr(settings,
    'MARKUPMIRROR_MARKDOWN_OUTPUT_FORMAT',
    'html5')

# Filter settings for reStructuredText
RESTRUCTUREDTEXT_FILTER = getattr(settings,
    'MARKUPMIRROR_RESTRUCTUREDTEXT_FILTER',
    {})

# Textile settings
TEXTILE_SETTINGS = getattr(settings,
    'MARKUPMIRROR_TEXTILE_SETTINGS',
    {'encoding': 'utf-8', 'output': 'utf-8'})


# Settings for MarkupMirrorContent for FeinCMS

# Init template for CodeMirror in FeinCMS
FEINCMS_INIT_TEMPLATE = getattr(settings,
    'MARKUPMIRROR_FEINCMS_INIT_TEMPLATE',
    'templates/admin/markupmirror/feincms/init_codemirror.html')

# Context for init template
FEINCMS_INIT_CONTEXT = getattr(settings,
    'MARKUPMIRROR_FEINCMS_INIT_CONTEXT', {
        'CODEMIRROR_JS': CODEMIRROR_JS,
        'CODEMIRROR_CSS': CODEMIRROR_CSS,
        'CODEMIRROR_PATH': CODEMIRROR_PATH,
        'CODEMIRROR_WIDTH': '50%',
        'CODEMIRROR_HEIGHT': '300px',
    })

FEINCMS_MARKUP_TYPE = getattr(settings,
    'MARKUPMIRROR_FEINCMS_MARKUP_TYPE', 'plaintext')
