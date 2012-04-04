from django.conf import settings

from markupmirror.markup import *


# Extensions for markdown
MARKDOWN_EXTENSIONS = getattr(settings,
    'MARKUPMIRROR_MARKDOWN_EXTENSIONS',
    ['extra', 'headerid(level=2)', 'sane_lists'])


# Filter settings for reStructuredText
RESTRUCTUREDTEXT_FILTER = getattr(settings,
    'MARKUPMIRROR_RESTRUCTUREDTEXT_FILTER',
    {})


# Textile settings
TEXTILE_SETTINGS = getattr(settings,
    'MARKUPMIRROR_TEXTILE_SETTINGS',
    {'encoding': 'utf-8', 'output': 'utf-8'})
