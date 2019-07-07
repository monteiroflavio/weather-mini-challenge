#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='weather-mini-challenge',
    version='0.0.1',
    description='Weather Mini Challenge',
    author='Flávio Monteiro',
    author_email='fm070795@gmail.com',
    url='http://my.cool.example.com',
    packages=['api','api.weather'],
    entry_points={
        'console_scripts': [
            'run = api.server:run'
        ],
    },
    package_dir={'api': 'api'},
    include_package_data=True,
    install_requires=['flask',],
    license="BSD",
    zip_safe=False,
    keywords='',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.4',
    ],
)