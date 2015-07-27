#!/usr/bin/env python
# coding: utf-8
from setuptools import setup, find_packages

setup(
    name='sequencer-edin1',
    version='0.0.1',
    url='https://github.com/edin1/sequencer-edin1',
    author="edin1",
    description="An implementation of the API http://docs.sequencer.apiary.io",
    install_requires=open("install_requires.txt").read().split(),
    packages=find_packages(exclude=['tests']),
    test_suite="tests",
    tests_require=open("tests_require.txt").read().split(),
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: System :: Monitoring',
    ),
    zip_safe=False,
)