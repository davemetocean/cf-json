# coding: utf-8
import sys
from setuptools import setup

NAME = "cfjson"
VERSION = "0.1"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["netcdf4"]

setup(
    name=NAME,
    version=VERSION,
    description="CF JSON converters",
    author_email="ops@metocean.co.nz",
    keywords=["CF-JSON"],
    packages=[NAME],
    requires=REQUIRES,
    long_description="""\
    Classes and functions for CF-JSON format conversion
    """
)
