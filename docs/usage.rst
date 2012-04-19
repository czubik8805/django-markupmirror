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

Markup types are registered with the ``markup_pool``.

Create your own Markup Type
---------------------------

Register and unregister Markup Types
------------------------------------


Using the ``MarkupMirrorField``
===============================


