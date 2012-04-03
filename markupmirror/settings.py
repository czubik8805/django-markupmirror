from django.conf import settings


# Extensions for markdown
MARKDOWN_EXTENSIONS = ','.join(settings.get(
    'MARKDOWNMIRROR_MARKDOWN_EXTENSIONS',
    ['abbr', 'def_list', 'footnotes', 'tables']))
