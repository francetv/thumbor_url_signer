#!/usr/bin/python
# -*- coding: utf-8 -*-

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license

from distutils.core import setup

setup(
    name = "thumbor_url_signer",
    packages = ["thumbor_url_signer"],
    version = "1.2.3",
    description = "Signer for Thumbor - Jeunesse Francetv Release",
    author = "Bertrand Thill",
    author_email = "bertrand.thill@francetv.fr",
    keywords = ["thumbor", "images", "signer"],
    license = 'MIT',
    url = 'https://github.com/francetv/thumbor_url_signer',
    classifiers = ['Development Status :: 4 - Beta',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: MIT License',
                   'Natural Language :: English',
                   'Operating System :: POSIX :: Linux',
                   'Programming Language :: Python :: 2.7',
                   'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
                   'Topic :: Multimedia :: Graphics :: Presentation'
    ],
    package_dir = {"thumbor_url_signer": "thumbor_url_signer"},
    install_requires=['thumbor>=6.5.0','pymongo>=3.4.0'],
    long_description = """\
This module provide s
"""
)