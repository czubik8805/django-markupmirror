from __future__ import absolute_import, unicode_literals


class MarkupError(Exception):
    """General execution error for markups."""


class InvalidMarkup(Exception):
    """Raised when a markup is not subclassing BaseMarkup."""
