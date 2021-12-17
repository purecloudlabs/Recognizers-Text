#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.

import os

from setuptools import setup, find_packages

path = "../libraries/recognizers-choice"

def read(fname):
    return open(os.path.join(path, fname)).read()

VERSION = "__version__"
ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

with io.open(os.path.join(ROOT_PATH, VERSION)) as f:
    version = f.readline()

NAME = 'recognizers-text-choice-genesys'
REQUIRES = ['recognizers-text', 'regex', 'grapheme']

setup(
    name=NAME,
    version=version,
    url='https://github.com/purecloudlabs/Recognizers-Text',
    author='Microsoft',
    description='recognizers-text-choice README',
    keywords=['nlp', 'nlp-entity-extraction',
              'entity-extraction', 'parser-library'],
    long_description=read('README.rst'),
    license='MIT',
    packages=find_packages(where=path),
    install_requires=REQUIRES,
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Development Status :: 3 - Alpha',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ]
)
