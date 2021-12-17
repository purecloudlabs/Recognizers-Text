import os, io
from setuptools import setup, find_packages

path = "libraries/recognizers-text"

curdir = os.getcwd()

def read(fname):
    return open(os.path.join(path, fname)).read()

VERSION_FILE = "__version__"

with io.open(os.path.join(curdir, "genesys_packages", VERSION_FILE)) as f:
    VERSION = f.readline()

NAME = "recognizers-text-genesys"
REQUIRES = ['emoji==1.1.0', 'multipledispatch']

setup(
    name=NAME,
    version=VERSION,
    url='https://github.com/Microsoft/Recognizers-Text',
    author='Microsoft',
    description='recognizers-text README',
    keywords=['nlp', 'nlp-entity-extraction',
              'entity-extraction', 'parser-library'],
    long_description='recognizers-text long README.',
    license='MIT',
    package_dir={'': path},
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
