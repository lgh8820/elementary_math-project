#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import os
from datetime import date
from setuptools import setup, find_packages

#--- import your package ---
import elementary_math as package


#--- Automatically generate setup parameters ---
# Your package name
PKG_NAME = package.__name__

# Your GitHub user name
GITHUB_USERNAME = package.__github_username__

# Short description will be the description on PyPI
try:
    SHORT_DESCRIPTION = package.__short_description__  # GitHub Short Description
except:
    print("'__short_description__' not found in '%s.__init__.py'!" % PKG_NAME)
    SHORT_DESCRIPTION = "No short description!"

# Long description will be the body of content on PyPI page
try:
    LONG_DESCRIPTION = open("README.rst", "rb").read().decode("utf-8")
except:
    LONG_DESCRIPTION = "No long description!"

# Version number, VERY IMPORTANT!
VERSION = package.__version__

# Author and Maintainer
try:
    AUTHOR = package.__author__
except:
    AUTHOR = "Unknown"

try:
    AUTHOR_EMAIL = package.__author_email__
except:
    AUTHOR_EMAIL = "Unknown"

try:
    MAINTAINER = package.__maintainer__
except:
    MAINTAINER = "Unknown"

try:
    MAINTAINER_EMAIL = package.__maintainer_email__
except:
    MAINTAINER_EMAIL = "Unknown"

# Include all sub packages in package directory
PACKAGES = [PKG_NAME] + ["%s.%s" % (PKG_NAME, i)
                         for i in find_packages(PKG_NAME)]

# Include everything in package directory
INCLUDE_PACKAGE_DATA = True
PACKAGE_DATA = {
    "": ["*.*"],
}

# The project directory name is the GitHub repository name
repository_name = os.path.basename(os.path.dirname(__file__))

# Project Url
URL = "https://github.com/{0}/{1}".format(GITHUB_USERNAME, repository_name)
# Use todays date as GitHub release tag
github_release_tag = str(date.today())
# Source code download url
DOWNLOAD_URL = "https://github.com/{0}/{1}/tarball/{2}".format(
    GITHUB_USERNAME, repository_name, github_release_tag)

try:
    LICENSE = package.__license__
except:
    print("'__license__' not found in '%s.__init__.py'!" % PKG_NAME)
    LICENSE = ""

PLATFORMS = [
    "Windows",
    "MacOS",
    "Unix",
]

CLASSIFIERS = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Natural Language :: English",
    "Operating System :: Microsoft :: Windows",
    "Operating System :: MacOS",
    "Operating System :: Unix",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3.4",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
]

try:
    f = open("requirements.txt", "rb")
    REQUIRES = [i.strip() for i in f.read().decode("utf-8").split("\n")]
except:
    print("'requirements.txt' not found!")
    REQUIRES = list()

setup(
    name=PKG_NAME,
    description=SHORT_DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    version=VERSION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    maintainer=MAINTAINER,
    maintainer_email=MAINTAINER_EMAIL,
    packages=PACKAGES,
    include_package_data=INCLUDE_PACKAGE_DATA,
    package_data=PACKAGE_DATA,
    url=URL,
    download_url=DOWNLOAD_URL,
    classifiers=CLASSIFIERS,
    platforms=PLATFORMS,
    license=LICENSE,
    install_requires=REQUIRES,
)

"""
Appendix
--------
::

Frequent used classifiers List = [
    "Development Status :: 1 - Planning",
    "Development Status :: 2 - Pre-Alpha",
    "Development Status :: 3 - Alpha",
    "Development Status :: 4 - Beta",
    "Development Status :: 5 - Production/Stable",
    "Development Status :: 6 - Mature",
    "Development Status :: 7 - Inactive",

    "Intended Audience :: Customer Service",
    "Intended Audience :: Developers",
    "Intended Audience :: Education",
    "Intended Audience :: End Users/Desktop",
    "Intended Audience :: Financial and Insurance Industry",
    "Intended Audience :: Healthcare Industry",
    "Intended Audience :: Information Technology",
    "Intended Audience :: Legal Industry",
    "Intended Audience :: Manufacturing",
    "Intended Audience :: Other Audience",
    "Intended Audience :: Religion",
    "Intended Audience :: Science/Research",
    "Intended Audience :: System Administrators",
    "Intended Audience :: Telecommunications Industry",

    "License :: OSI Approved :: BSD License",
    "License :: OSI Approved :: MIT License",
    "License :: OSI Approved :: Apache Software License",
    "License :: OSI Approved :: GNU General Public License (GPL)",
    "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",

    "Natural Language :: English",
    "Natural Language :: Chinese (Simplified)",

    "Operating System :: Microsoft :: Windows",
    "Operating System :: MacOS",
    "Operating System :: Unix",
    
    "Programming Language :: Python",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 2 :: Only",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.4",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3 :: Only",
]
"""
