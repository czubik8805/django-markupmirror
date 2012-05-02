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

.. _Markdown: http://daringfireball.net/projects/markdown/
.. _reStructuredText: http://docutils.sourceforge.net/rst.html
.. _Textile: http://www.textism.com/tools/textile/

The Markup Pool
---------------

The markup pool is the main access point to markup converters. They are
registered with the pool, and retrieved from it.

.. py:data:: markupmirror.markup.base.markup_pool

   Instance of ``MarkupPool`` for public use.

.. autoclass:: markupmirror.markup.base.MarkupPool
   :members:

Create your own Markup Type
---------------------------

You can easily create your own markup converters for any purpose. The converter
only needs to inherit from ``BaseMarkup`` and implement the ``convert`` method.

.. autoclass:: markupmirror.markup.base.BaseMarkup
   :members: convert, before_convert, after_convert, __call__, get_name
   :special-members:

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

Using the ``MarkupMirrorField``
===============================


