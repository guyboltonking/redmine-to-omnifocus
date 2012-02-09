#!/usr/bin/env python

from setuptools import setup

setup(name='redmine-to-omnifocus',
      version='1.0',
      description='Import Redmine issues into OmniFocus',
      author='Guy Bolton King',
      author_email='guy@waftex.com',
      url='https://github.com/guyboltonking/redmine-to-omnifocus',
      classifiers=['Development Status :: 5 - Production/Stable',
                   'License :: OSI Approved :: MIT License',
                   'Programming Language :: Python :: 2.7',
                   'Topic :: Software Development :: Bug Tracking',
                   'Operating System :: MacOS :: MacOS X'],
      install_requires=['BeautifulSoup>=3.0',
                        'appscript>=0.20',
                        'gntp'],
      scripts=['redmine-to-omnifocus'])
