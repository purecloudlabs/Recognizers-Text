#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.

from setuptools import setup, find_packages
import os, io

path = "../libraries/recognizers-text"

VERSION = "__version__"

with io.open(os.path.join("..", VERSION)) as f:
    version = f.readline()

NAME = "recognizers-text"
REQUIRES = ['emoji==1.1.0', 'multipledispatch']

setup(
    name=NAME,
    version=version,
    url='https://github.com/Microsoft/Recognizers-Text',
    author='Microsoft',
    description='recognizers-text README',
    keywords=['nlp', 'nlp-entity-extraction',
              'entity-extraction', 'parser-library'],
    long_description='recognizers-text long README.',
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
