# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='dyndnsimple',
    version='0.0.1',
    description='Package for updating DNSimple domain with an IP address.',
    long_description=readme,
    author='Ben Hughes',
    author_email='bwghughes@gmail.com',
    url='https://github.com/bwghughes/dyndnsimple',
    license=license,
    packages=find_packages(exclude=('tests', 'docs', 'config'))
)
