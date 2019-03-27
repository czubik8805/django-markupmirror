from __future__ import absolute_import, unicode_literals

import logging
from importlib import import_module

try:
    from django.utils.encoding import smart_text, smart_bytes
except ImportError:
    from django.utils.encoding import (
        smart_unicode as smart_text, smart_str as smart_bytes)

from markupmirror.exceptions import *
from markupmirror import settings


__all__ = ('markup_pool', 'register_markup', 'BaseMarkup')


LOG = logging.getLogger("markupmirror")


class BaseMarkup(object):
    """Basic interface for markup converter classes.

    An example converter could look like this::

        class ExampleMarkup(BaseMarkup):

            def convert(self, markup):
                return markup.replace("example", "markup")

    """
    codemirror_mode = ''
    title = ""
    requires = {}
    _requirements = {}

    @classmethod
    def get_name(cls):
        """Returns lowercase markup name, without the "Markup" part.

        Class naming convention is ``<Markup-Type>Markup``.
        """
        return cls.__name__.replace("Markup", "", 1).lower()

    @property
    def requirements(self):
        """Provide access to loaded requirements."""
        return self._requirements

    def convert(self, markup, *args, **kwargs):
        """Main conversion method. Must be implemented in subclasses."""
        return markup

    def before_convert(self, markup, *args, **kwargs):
        """Called before ``convert``. Can be used to separate the main
        conversion through a third-party library (e.g. Markdown) from
        additional logic.

        """
        return markup

    def after_convert(self, markup, *args, **kwargs):
        """Called after ``convert``. Similar to ``before_convert``."""
        return markup

    def __call__(self, markup, *args, **kwargs):
        """Main entry point. Calls ``before_convert``, ``convert`` and
        ``after_convert`` in that order.

        """
        converted = self.before_convert(markup, *args, **kwargs)
        converted = self.convert(converted, *args, **kwargs)
        converted = self.after_convert(converted, *args, **kwargs)
        return smart_text(converted)


class MarkupPool(object):
    """Pool for markup converters.

    Each markup class, subclassing
    ``markupmirror.markup.base.BaseMarkup``, must register to this
    pool using ``register_markup`` defined below.

    """
    def __init__(self):
        self._markups = None

    @property
    def markups(self):
        """List registered markup types.

        Defaults to the ``MARKUPMIRROR_MARKUP_TYPES`` defined in settings.

        First access loads and registeres the configured markup converters
        with this pool.

        """
        if self._markups is None:
            self._markups = {}
            for markup in settings.MARKUPMIRROR_MARKUP_TYPES.values():
                markup = self.load_markup(markup)
                if markup is not None:
                    self.register_markup(markup)
        return self._markups

    def register_markup(self, markup):
        """Registers a markup converter class.

        ``markup`` must be a subclass of ``BaseMarkup`` and may not be
        registered already.

        """
        # check for correct subclassing
        if not issubclass(markup, BaseMarkup):
            raise InvalidMarkup(
                "Markups must be subclasses of "
                "markupmirror.markup.base.BaseMarkup. %r is not."
                % markup)

        markup_name = markup.get_name()

        # Make sure we can import all the required modules
        if markup.requires:
            failed = self.load_requirements(markup)
            if failed:
                errors = "\n\t".join(
                    "%s:%s" % (requirement, error)
                    for requirement, error in failed)
                LOG.warning(
                    "Couldn't register markup %s:%s\n\t%s",
                    markup_name, markup, errors)
                return

        self.markups[markup_name] = markup()

    def load_markup(self, markup):
        """Import markup converter class from specified path.

        If already an object, then return as is otherwise, import it first.

        """
        if not isinstance(markup, str):
            return markup

        markup = smart_bytes(markup)
        parts = markup.split(b'.')
        name = parts[-1]
        leadup = b'.'.join(parts[:-1])
        loaded = import_module(leadup.decode("utf-8"))
        return getattr(loaded, name.decode("utf-8"))

    def load_requirements(self, markup):
        """See that we can import everything in the requires field.

        Return list of [(requirement, error), ...]
        for all the requirements that couldn't be fullfilled

        """
        failed = []

        for requirement, import_path in markup.requires.items():
            import_path = smart_bytes(import_path)
            parts = import_path.split(b'.')
            try:
                req_callable = parts[-1]
                leadup = b'.'.join(parts[:-1])
                loaded = import_module(leadup.decode("utf-8"))
                markup._requirements[requirement] = getattr(loaded, req_callable.decode("utf-8"))
            except ImportError as error:
                failed.append((requirement, error))

        return failed

    def unregister_markup(self, markup_name):
        """Unregisters a markup converter with the name ``markup_name``.
        Fails silently if no converter was registered by that name.

        Alternatively you can also use the ``del`` operator::

           del markup_pool['restructuredtext']

        """
        if markup_name in self.markups:
            del self.markups[markup_name]

    def has_markup(self, markup_name):
        """Tests if a markup converter with the name ``markup_name`` is already
        registered with the markup pool.

        Alternatively you can also use the ``in`` operator, like with a
        dictionary::

            if 'restructuredtext' in markup_pool:
                pass

        """
        return markup_name in self.markups

    def get_markup(self, markup_name):
        """Returns one markup converter by name.
        Raises ``KeyError`` if no converter was registered by ``markup_name``.

        Alternatively you can also use the ``[]`` accessor, like with a
        dictionary::

            markup = markup_pool['restructuredtext']

        """
        return self.markups[markup_name]

    def __contains__(self, key):
        return self.has_markup(key)

    def __getitem__(self, key):
        return self.get_markup(key)

    def __delitem__(self, key):
        self.unregister_markup(key)


markup_pool = MarkupPool()  # Instance of ``MarkupPool`` for public use.
register_markup = markup_pool.register_markup
