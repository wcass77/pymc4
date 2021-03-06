import codecs
import re
from pathlib import Path

from setuptools import setup, find_packages


PROJECT_ROOT = Path(__file__).resolve().parent
REQUIREMENTS_FILE = PROJECT_ROOT / "requirements.txt"
REQUIREMENTS_DEV_FILE = PROJECT_ROOT / "requirements-dev.txt"
README_FILE = PROJECT_ROOT / "README.md"
VERSION_FILE = PROJECT_ROOT / "pymc4" / "__init__.py"

NAME = "pymc4"
DESCRIPTION = "A Python probabilistic programming interface to TensorFlow, for Bayesian modelling and machine learning."
AUTHOR = "PyMC Developers"
AUTHOR_EMAIL = "pymc.devs@gmail.com"
URL = "https://github.com/pymc-devs/pymc4"
LICENSE = "Apache License, Version 2.0"

CLASSIFIERS = [
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "License :: OSI Approved :: Apache Software License",
    "Intended Audience :: Science/Research",
    "Topic :: Scientific/Engineering",
    "Topic :: Scientific/Engineering :: Mathematics",
    "Operating System :: OS Independent",
]


def get_requirements(path):
    with codecs.open(path) as buff:
        return buff.read().splitlines()


def get_long_description():
    with codecs.open(README_FILE, "rt") as buff:
        return buff.read()


def get_version():
    lines = open(VERSION_FILE, "rt").readlines()
    version_regex = r"^__version__ = ['\"]([^'\"]*)['\"]"
    for line in lines:
        mo = re.search(version_regex, line, re.M)
        if mo:
            return mo.group(1)
    raise RuntimeError("Unable to find version in %s." % (VERSION_FILE,))


if __name__ == "__main__":
    setup(
        name=NAME,
        version=get_version(),
        description=DESCRIPTION,
        license=LICENSE,
        author=AUTHOR,
        author_email=AUTHOR_EMAIL,
        url=URL,
        classifiers=CLASSIFIERS,
        packages=find_packages(),
        install_requires=get_requirements(REQUIREMENTS_FILE),
        tests_require=get_requirements(REQUIREMENTS_DEV_FILE),
        long_description=get_long_description(),
        long_description_content_type="text/markdown",
        include_package_data=True,
    )
