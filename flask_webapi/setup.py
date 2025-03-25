#!/usr/bin/env python
import re
from os import path
from setuptools import setup, find_packages

version_file = path.join(
    path.dirname(__file__),
    'flask_restful',
    '__version__.py'
)
with open(version_file, 'r') as fp:
    m = re.search(
        r"^__version__ = ['\"]([^'\"]*)['\"]",
        fp.read(),
        re.M
    )
    version = m.groups(1)[0]


setup(
    name='Flask-WebApi',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'flask>=3.1.0',
    ],
    license='MIT',
    classifiers=[
        'Framework :: Flask',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'License :: OSI Approved :: MIT License',
    ],
    author='Jesus Otero',
    author_email='jesusoterove@gmail.com',
    description='Python Webapi for flask done dotnet style',
    url='https://github.com/jesusoterove/Flask-WebApi',
)
