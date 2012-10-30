# -*- coding: utf-8 -*-
import dyndnsimple
from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

requires = ['requests==0.14.1']

scripts = ['scripts/dyndnsimple']

setup(
    name='dyndnsimple',
    version="0.0.11",
    description='Package for updating DNSimple domain with a WAN IP address.',
    long_description=readme,
    author='Ben Hughes',
    author_email='bwghughes@gmail.com',
    url='https://github.com/bwghughes/dyndnsimple',
    license=license,
    install_requires=requires,
    scripts=scripts,
    packages=find_packages(exclude=('test')),
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ),
)
