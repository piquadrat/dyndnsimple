# -*- coding: utf-8 -*-
from dyndnsimple import __version__ as version
from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='dyndnsimple',
    version=version,
    description='Package for updating DNSimple domain with a WAN IP address.',
    long_description=readme,
    author='Ben Hughes',
    author_email='bwghughes@gmail.com',
    url='https://github.com/bwghughes/dyndnsimple',
    license=license,
    packages=find_packages(exclude=('test', 'docs', 'config')),
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ),
)
