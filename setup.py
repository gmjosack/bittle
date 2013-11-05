#!/usr/bin/env python

from distutils.core import setup

execfile('bittle/version.py')

kwargs = {
    "name": "bittle",
    "version": str(__version__),
    "packages": ["bittle", "bittle.tests"],
    "description": "Simple library to help with bit manipulations.",
    # PyPi, despite not parsing markdown, will prefer the README.md to the
    # standard README. Explicitly read it here.
    "long_description": open("README").read(),
    "author": "Gary M. Josack",
    "maintainer": "Gary M. Josack",
    "author_email": "gary@byoteki.com",
    "maintainer_email": "gary@byoteki.com",
    "license": "MIT",
    "url": "https://github.com/gmjosack/bittle",
    "download_url": "https://github.com/gmjosack/bittle/archive/master.tar.gz",
    "classifiers": [
        "Programming Language :: Python",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ]
}

setup(**kwargs)
