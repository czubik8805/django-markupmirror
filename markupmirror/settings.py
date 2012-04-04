from django.conf import settings


# Extensions for markdown
MARKDOWN_EXTENSIONS = settings.get(
    'MARKUPMIRROR_MARKDOWN_EXTENSIONS',
    ['extra', 'headerid(level=2)', 'sane_lists'])


# Filter settings for reStructuredText
RESTRUCTUREDTEXT_FILTER = settings.get(
    'MARKUPMIRROR_RESTRUCTUREDTEXT_FILTER',
    settings.RESTRUCTUREDTEXT_FILTER_SETTINGS)


# Textile settings
TEXTILE_SETTINGS = settings.get(
    'MARKUPMIRROR_TEXTILE_SETTINGS',
    {'encoding': 'utf-8', 'output': 'utf-8'})
