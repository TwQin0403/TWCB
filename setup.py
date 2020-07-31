# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='TWCB',
    version='0.1.0',
    description='Sample package for Python-Guide.org',
    long_description=readme,
    author='Qin Wei Zhi',
    author_email='p300053000qin@gmail.com',
    url='https://github.com/TwQin0403/TWCB',
    license=license,
    packages=find_packages(exclude=('tests'))
)

