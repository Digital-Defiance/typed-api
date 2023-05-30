from setuptools import setup, find_packages

import os

VERSION = os.getenv('PACKAGE_VERSION', None)

if VERSION is None:
  raise RuntimeError('`PACKAGE_VERSION` not defined.')

setup(
    name='typed-api',
    version=VERSION,
    description='A lightweigt package for concisely defining an api.',
    author='Rui Filipe de Sousa Campos @ Digital Defiance',
    author_email='mail@ruicampos.org',
    url='https://github.com/Digital-Defiance/typed-api',
    packages=find_packages(),
    long_description="A lightweigt package for concisely defining an api.",
    long_description_content_type="text/markdown",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
)