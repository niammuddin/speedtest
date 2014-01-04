#!/usr/bin/env python

import setuptools

setuptools.setup(
    name='speedtest-cli',
    version='0.2.4',
    description=('Command line interface for testing internet bandwidth using '
                 'speedtest.net'),
    long_description=open('README.rst').read(),
    author='Matt Martz',
    author_email='matt@sivel.net',
    url='https://github.com/sivel/speedtest-cli',
    license='Apache License, Version 2.0',
    py_modules=['speedtest_cli'],
    entry_points={
        'console_scripts': [
            'speedtest=speedtest_cli:main',
            'speedtest-cli=speedtest_cli:main'
        ]
    },
    classifiers=[
        'Programming Language :: Python',
        'Environment :: Console',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent'
    ]
)
