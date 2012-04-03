import os

from setuptools import setup
from setuptools import find_packages


PROJECT_NAME = "markupmirror"
AUTHORS = (
    (u"Fabian B\xfcchler", "fabian.buechler@gmail.com"),
)


def read(*parts):
    path = os.path.abspath(os.path.join(os.path.dirname(__file__), *parts))
    content = ""
    with open(path) as fp:
        content = fp.read()
    return content


setup(
    name=PROJECT_NAME,
    version=__import__(PROJECT_NAME).get_version(),
    author=", ".join([a[0] for a in AUTHORS]),
    author_email=", ".join([a[1] for a in AUTHORS]),
    description="Django field and widget for editing markup content.",
    long_description="{0}\n\n{1}".format(
        read('README.rst'),
        read('docs', 'changelog.rst')),
    url="https://bitbucket.org/fabianbuechler/django-markupmirror",
    keywords="django markup field widget codemirror",
    license="BSD License",
    platforms=["OS Independent"],
    zip_safe=False,
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Development Status :: 2 - Pre-Alpha"
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: JavaScript",
        "Environment :: Web Environment",
    ],
)
