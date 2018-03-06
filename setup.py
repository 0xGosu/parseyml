#!/usr/bin/python
# -*- coding: utf-8 -*-   
#
#  setup.py
#  
#
#  Created by TVA on 1/25/18.
#  Copyright (c) 2018 parseyml. All rights reserved.
#
from __future__ import unicode_literals
from setuptools import setup, find_packages
import os

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'parseyml/VERSION')) as f:
    __version__ = f.read()

setup(
    name='parseyml',
    version=__version__,
    description='A python executable script to parse yml file and export to shell environment',
    author='V.Anh Tran',
    author_email='tranvietanh1991@gmail.com',
    license="MIT",
    url='https://github.com/tranvietanh1991/parseyml',  # use the URL to the github repo
    download_url='https://github.com/tranvietanh1991/parseyml/archive/master.zip',  # source code download
    packages=find_packages(exclude=['*.tests', '*.tests.*']),
    scripts=['bin/parseyml'],
    include_package_data=True,
    install_requires=[
        "PyYAML>=3.11",
    ],
    python_requires='>=2.6, <3',
    keywords=['yaml', 'parse', 'parseyml', 'parse-yml', 'yml', 'export', 'shell'],  # arbitrary keywords
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        # "Framework :: Django",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        # "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
