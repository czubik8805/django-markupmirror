.. _installation:

==============
 Installation
==============

* To **install** django-markupmirror, use `pip`_ (or `easy_install`_ or simply
  ``python setup.py install`` from source) and add ``'markupmirror'`` to the
  ``INSTALLED_APPS`` in your `Django`_ project.

  .. code-block:: bash

    $ pip install django-markupmirror

  ::

    INSTALLED_APPS = (
        ...
        'markupmirror',
        ...
    )

* In your ``settings.py`` specify at least ``MARKUPMIRROR_DEFAULT_MARKUP_TYPE``
  which is ``'plaintext'`` by default.

* For the markup HTML-preview, you'll need to add markupmirror's URLs in your
  URLconf. In your ``urls.py`` add::

    import markupmirror.urls

    urlpatterns = patterns('',
        (r'^markupmirror/', include(markupmirror.urls.preview)),
    )

.. _pip: http://www.pip-installer.org/
.. _easy_install: http://peak.telecommunity.com/DevCenter/EasyInstall

Requirements
------------

django-markupmirror depends on:

* `Django`_ 1.4+ (for now tested with 1.4 only), obviously.

* `FeinCMS`_ 1.5+ (for now tested with 1.5.3 only), if you want to use the page
  content-type.

* `Markdown 2.1+`_, if you want to use the ``MarkdownMarkup`` converter.

* `Docutils 0.8+`_, if you want to use the ``ReStructuredTextMarkup``
  converter.

* `Textile 2.1+`_, if you want to use the ``TextileMarkup`` converter.

The three latter will be available automatically if the respective dependencies
are met.

.. _Django: http://pypi.python.org/pypi/Django
.. _FeinCMS: http://pypi.python.org/pypi/FeinCMS
.. _Markdown 2.1+: http://pypi.python.org/pypi/Markdown
.. _Docutils 0.8+: http://pypi.python.org/pypi/docutils
.. _Textile 2.1+: http://pypi.python.org/pypi/textile

Settings & Configuration
------------------------

Use the configuration variables below in your ``settings.py`` to customize the
behaviour of django-markupmirror:

.. automodule:: markupmirror.settings
   :members:
