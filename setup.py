from __future__ import absolute_import, unicode_literals
import os
import pathlib
import textwrap

from setuptools import setup
from setuptools import find_packages


AUTHORS = (
    ("Fabian B\xfcchler", "fabian.buechler@gmail.com"),
)


def read(*parts):
    path = os.path.abspath(os.path.join(os.path.dirname(__file__), *parts))
    return pathlib.Path(path).read_text()


setup(
    name='django-markupmirror',
    version="0.5a1",
    author=", ".join([a[0] for a in AUTHORS]),
    author_email=", ".join([a[1] for a in AUTHORS]),
    description=textwrap.dedent("""\
        Django field and widget for editing markup content (PlainText, HTML,
        Markdown, reStructuredText, Textile) using the CodeMirror editor with
        live preview."""),
    long_description='\n\n'.join([
        read('README.rst'),
        read('docs', 'quickstart.rst'),
        read('docs', 'changelog.rst'),
    ]),
    url="https://bitbucket.org/fabianbuechler/django-markupmirror",
    keywords="django markup field widget codemirror",
    license="BSD License",
    platforms=["OS Independent"],
    zip_safe=False,
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: JavaScript",
        "Environment :: Web Environment",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: Markup",
    ],
)
