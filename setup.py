#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='ThePirateBay',
    version='1.1.0',
    install_requires=['BeautifulSoup4', 'purl', 'dateutils', 'lxml'],
    author='Karan Goel',
    author_email='karan@goel.im',
    packages=['tpb','tests'],
    test_suite='tests',
    url='https://github.com/thekarangoel/TPB/',
    license='GNU General Public License',
    description='Unofficial Python API for ThePirateBay.',
    long_description='Unofficial Python API for ThePirateBay. Usage: https://github.com/thekarangoel/TPB.',
)
