import os
from setuptools import setup, find_packages

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
    long_description = 'Thumbor signer adapters'


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="thumbor_url_signer",
    version="1.0.0",
    author="Bertrand THILL",
    description=("Thumbor thumbor signer adapters - France.tv Release"),
    license="MIT",
    keywords="thumbor mongodb mongo",
    url="https://github.com/francetv/thumbor_url_signer",
    packages=[
        'thumbor_url_signer',
        'thumbor_url_signer.url_signer'
    ],
    long_description=long_description,
    classifiers=[
        'Development Status ::4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
    ],
    install_requires=[
        'thumbor>=6.7.0'
    ]
)
