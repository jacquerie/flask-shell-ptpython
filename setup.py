# -*- coding: utf-8 -*-

"""Replace the default ``flask shell`` command with a similar one running PTPython."""

from __future__ import absolute_import, division, print_function

from setuptools import setup


URL = 'https://github.com/jacquerie/flask-shell-ptpython'

readme = open('README.rst').read()

setup_requires = [
    'autosemver~=0.0,>=0.5.2',
]

install_requires = [
    'Flask~=0.0,>=0.12.2',
    'click~=6.0,>=6.7',
    'ptpython~=0.0,>=0.41',
]

docs_require = []

tests_require = [
    'flake8-future-import~=0.0,>=0.4.3',
    'pytest-flake8~=0.0,>=.0.9.1',
    'pytest~=3.0,>=3.2.3',
]

extras_require = {
    'docs': docs_require,
    'tests': tests_require,
}

extras_require['all'] = []
for name, reqs in extras_require.items():
    extras_require['all'].extend(reqs)

setup(
    name='flask-shell-ptpython',
    autosemver={
        'bugtracker_url': URL + '/issues',
    },
    url=URL,
    license='MIT',
    author='Jacopo Notarstefano',
    author_email='jacopo.notarstefano@gmail.com',
    py_modules=['flask_shell_ptpython'],
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    description=__doc__,
    long_description=readme,
    setup_requires=setup_requires,
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require=extras_require,
    entry_points={
        'flask.commands': [
            'shell=flask_shell_ptpython:shell_command',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python',
    ],
)
