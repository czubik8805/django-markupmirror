from __future__ import absolute_import, unicode_literals

try:
    import feincms
except ImportError:
    raise ImportError(
        "FeinCMS is required to use markupmirror.feincms.MarkupMirrorContent.")
