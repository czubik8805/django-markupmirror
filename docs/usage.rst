.. _usage:

=======
 Usage
=======

Markup-Types
============

django-markupmirror comes with five default markup types (or converters). You
Can create and register your own converters and unregister the default ones if
you prefer.

.. _usage-markup-types-default:

Default Markup Types
--------------------

The markup-types available by default are:

``plaintext``
    .. automodule:: markupmirror.markup.plaintext
    .. autoclass:: PlainTextMarkup

``html``
    .. automodule:: markupmirror.markup.html
    .. autoclass:: HtmlMarkup

``markdown``
    .. automodule:: markupmirror.markup.markdown_
    .. autoclass:: MarkdownMarkup

``restructuredtext``
    .. automodule:: markupmirror.markup.restructuredtext
    .. autoclass:: ReStructuredTextMarkup

``textile``
    .. automodule:: markupmirror.markup.textile_
    .. autoclass:: TextileMarkup

The Markup Pool
---------------

The markup pool is the main access point to markup converters. They are
registered with the pool, and retrieved from it.

..  automodule:: markupmirror.markup.base

..  py:data:: markupmirror.markup.base.markup_pool

    Instance of ``MarkupPool`` for public use.

..  autoclass:: MarkupPool
    :members:

Create your own Markup Type
---------------------------

You can easily create your own markup converters for any purpose. The converter
only needs to inherit from ``BaseMarkup`` and implement the ``convert`` method.

..  autoclass:: markupmirror.markup.base.BaseMarkup
    :members: convert, before_convert, after_convert, __call__, get_name
    :special-members:

..  note::
    If ``convert``, ``before_convert`` or ``after_convert`` accept
    ``*args`` and ``**kwargs`` which can be exploited to pass the request or a
    model instance into the conversion process.

It may also have a ``requires`` dictionary attribute that defines named
requirements by their full import path.

When the markup type is registered, these ``requires`` will be resolved and
made available through the ``requirement`` attribute (also a dictionary) of the
markup class.

For example:

..  code-block:: python

    from markupmirror.markup.base import BaseMarkup

    class ExampleMarkup(BaseMarkup):

        requires = {
            'wikimarkup': wikimarkup.parse',
        }

        def convert(self, markup):
            return self.requirements['wikimarkup'](markup)

If any requirements can't be resolved then the ``markupmirror`` logger will
emit a warning complaining about this and the markup type is not registered.

Register and unregister Markup Types
------------------------------------

The :ref:`default markup types <usage-markup-types-default>` provided by
django-markupmirror are registered during initialization. If you want to remove
any of these, you can use the ``MarkupPool.unregister_markup`` method::

    from markupmirror.markup.base import markup_pool

    markup_pool.unregister_markup('plaintext')  # is equal to
    del markup_pool['textile']

To register new markup converters, pass the markup class to the
``MarkupPool.register_markup`` method::

    from markupmirror.markup.base import markup_pool, BaseMarkup

    class ExampleMarkup(BaseMarkup):

        def convert(self, markup):
            return markup.replace("markup", "example")

    markup_pool.register_markup(ExampleMarkup)

This would make the ``ExampleMarkup`` converter available through the key
``example``, derived from its class name::

    example_markup = markup_pool['example']

Registration via settings.py
----------------------------

You may also control what markup types are registered on initialisation via
the following two settings in your project's settings.py:

    MARKUPMIRROR_IGNORE_DEFAULT_TYPES
        Whether to ignore all default markup types

    MARKUPMIRROR_MARKUP_TYPES
        Dictionary of key to markup type.

        Where markup type is either an subclass of ``BaseMarkup``
        or a dot seperated import path to a subclass of ``BaseMarkup``.

        These will be merged on top of the default markup types.

Using the ``MarkupMirrorField``
===============================

After you have configured markupmirror in your settings and added your custom
markup converters, the only thing left to do is to use the
``MarkupMirrorField`` in your models.

A field with fixed markup type would have to provide a ``markup_type``::

    from django.db import models
    from markupmirror.fields import MarkupMirrorField

    class MyModel(models.Model):
        content = MarkupMirrorField(markup_type='markdown')

To provide a selectbox for the users to select the content's markup type
manually, use ``default_markup_type`` instead::

    class MyModel(models.Model):
        content = MarkupMirrorField(default_markup_type='plaintext')

If you provide neither ``markup_type`` nor ``default_markup_type``, the
``MARKUPMIRROR_DEFAULT_MARKUP_TYPE`` setting will be used as default.

For reference, see the ``MarkupMirrorField`` and ``Markup`` classes:

..  automodule:: markupmirror.fields

..  autoclass:: MarkupMirrorField

..  autoclass:: Markup
    :members: raw, markup_type, rendered, __unicode__
    :special-members:
