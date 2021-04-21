#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=6.0',
                'googletrans==3.0.0',
                'polib==1.1.1',
                'path.py==12.5.0',
                'importlib_resources==5.1.2',
                ]

setup_requirements = ['pytest-runner', ]

test_requirements = ['pip==21.0.1',
                     'pytest==6.2.3',
                     'pytest-runner==5.3.0',
                     'Click>=6.0',
                     'bump2version==1.0.1',
                     'wheel==0.36.2',
                     'watchdog==2.0.2',
                     'flake8==3.9.1',
                     'tox==3.23.0',
                     'coverage==5.5',
                     'Sphinx==3.5.4',
                     'twine==3.4.1',
                     'googletrans==3.0.0',
                     'polib==1.1.1',
                     'importlib_resources==5.1.2',
                     ]

extras_require = {
    'transifex': [
        'transifex_client>=0.14.2'
    ],
}

setup(
    version='1.1.5',
    author="SekouD",
    author_email='sekoud.python@gmail.com',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Operating System :: MacOS',
        'Operating System :: Microsoft',
        'Operating System :: POSIX',
        'Natural Language :: Afrikaans', 'Natural Language :: Arabic','Natural Language :: German',
        'Natural Language :: Greek', 'Natural Language :: English', 'Natural Language :: French',
        'Natural Language :: Italian', 'Natural Language :: Japanese',
        'Natural Language :: Chinese (Simplified)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    description="A python package to easily translate po and pot files in any language supported by Google Translate.",
    entry_points={
        'console_scripts': [
            'potranslator=potranslator.commands:main',
        ],
    },
    install_requires=requirements,
    license="BSD license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    package_data={'translations': ['potranslator/locale_dir/*'],
                  'tests': ['tests/*'],
                  'type_stubs': ['potranslator/py.typed', 'potranslator/*']},
    keywords='potranslator sphinx sphinx-intl gettext localization translation translate po pot mo internationalization python google',
    name='potranslator',
    packages=find_packages(include=['potranslator']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/SekouD/potranslator',
    zip_safe=False,
)
