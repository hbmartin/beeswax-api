# -*- coding: utf-8 -*-
#
# This file were created by Python Boilerplate. Use boilerplate to start simple
# usable and best-practices compliant Python projects.
#
# Learn more about it at: http://github.com/fabiommendes/python-boilerplate/
#

import os
import codecs
from setuptools import setup, find_packages

# Save version and author to __meta__.py
version = open('VERSION').read().strip()
dirname = os.path.dirname(__file__)
path = os.path.join(dirname, 'src', 'beeswax_api', '__meta__.py')
meta = '''# Automatically created. Please do not edit.
__version__ = '%s'
__author__ = 'Harold Martin'
''' % version
with open(path, 'w') as F:
    F.write(meta)

setup(
    # Basic info
    name='beeswax-api',
    version=version,
    author='Harold Martin',
    author_email='harold.martin@grindr.com',
    url='https://github.com/hbmartin/beeswax-api',
    description='Client for the Beeswax API',
    long_description=codecs.open('README.rst', 'rb', 'utf8').read(),
    license='Apache License Version 2.0',

    # Classifiers (see https://pypi.python.org/pypi?%3Aaction=list_classifiers)
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: Apache Software License',
    ],

    # Packages and dependencies
    package_dir={'': 'src'},
    packages=find_packages('src'),
    install_requires=[],
    extras_require={},

    # Other configurations
    zip_safe=False,
    platforms='any',
)
