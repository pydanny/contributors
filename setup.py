#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
from setuptools import setup
import sys

version = "0.3.0"

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    'github3.py==1.0.0a4'
]

test_requirements = [
    # TODO: put package test requirements here
]

if sys.argv[-1] == 'publish':
    try:
        import wheel
        print("Wheel version: ", wheel.__version__)
    except ImportError:
        print('Wheel library missing. Please run "pip install wheel"')
        sys.exit()
    os.system('python setup.py sdist upload')
    os.system('python setup.py bdist_wheel upload')
    sys.exit()

if sys.argv[-1] == 'tag':
    print("Tagging the version on github:")
    os.system("git tag -a %s -m 'version %s'" % (version, version))
    os.system("git push --tags")
    sys.exit()

setup(
    name='contributors',
    version=version,
    description="A command-line script to get all the contributors for one or more GitHub projects.",
    long_description=readme + '\n\n' + history,
    author="Daniel Roy Greenfeld",
    author_email='pydanny@gmail.com',
    url='https://github.com/pydanny/contributors',
    packages=[
        'contributors',
    ],
    package_dir={'contributors':
                 'contributors'},
    entry_points={
        'console_scripts': [
            'contributors=contributors.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="Apache Software License 2.0",
    zip_safe=False,
    keywords='contributors',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
