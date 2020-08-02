# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


with open('README.rst','r',encoding='utf-8') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

with open('requirements.txt') as fid:
    requires = [line.strip() for line in fid]

setup(
    name='TWCB',
    version='0.1.0',
    description='Third API for TWCB',
    long_description=readme,
    author='Qin Wei Zhi',
    author_email='p300053000qin@gmail.com',
    url='https://github.com/TwQin0403/TWCB',
    license=license,
    install_requires=requires,
    packages=find_packages(exclude=('tests'))
)

