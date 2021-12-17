import os, io
from setuptools import setup, find_packages

path = "libraries/recognizers-choice"

curdir = os.getcwd()

def read(fname):
    return open(os.path.join(path, fname)).read()

VERSION_FILE = "__version__"

with io.open(os.path.join(curdir, "genesys_packages", VERSION_FILE)) as f:
    VERSION = f.readline()

NAME = 'recognizers-text-choice-genesys'
REQUIRES = ['recognizers-text-genesys', 'regex', 'grapheme']

setup(
    name=NAME,
    version=VERSION,
    url='https://github.com/purecloudlabs/Recognizers-Text',
    author='Microsoft',
    description='recognizers-text-choice README',
    keywords=['nlp', 'nlp-entity-extraction',
              'entity-extraction', 'parser-library'],
    long_description=read('README.rst'),
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
