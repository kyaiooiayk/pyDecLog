import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent


PACKAGE_NAME = "pyDecLog"
AUTHOR = "kyaiooiayk"
AUTHOR_EMAIL = "kayaiooiayk@email.com"
URL = "https://github.com/kyaiooiayk/pyDecLog"
DOWNLOAD_URL = "https://pypi.org/project/pyDecLog/"

LICENSE = "MIT"
VERSION = (HERE / "VERSION").read_text(encoding="utf8").strip()
DESCRIPTION = "pyDecLog: a Python module for logging via decorators"
LONG_DESCRIPTION = (HERE / "README.md").read_text()
LONG_DESC_TYPE = "text/markdown"

requirements = (HERE / "requirements.txt").read_text(encoding="utf8")
INSTALL_REQUIRES = [s.strip() for s in requirements.split("\n")]

dev_requirements = (HERE / "requirements_dev.txt").read_text(encoding="utf8")
EXTRAS_REQUIRES = {"dev": [s.strip() for s in dev_requirements.split("\n")]}

CLASSIFIERS = [
    f"Programming Language :: Python :: 3.{str(v)}" for v in range(9, 10)
]

PYTHON_REQUIRES = ">=3.9"

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESC_TYPE,
    author=AUTHOR,
    license=LICENSE,
    author_email=AUTHOR_EMAIL,
    url=URL,
    python_requires=PYTHON_REQUIRES,
    install_requires=INSTALL_REQUIRES,
    extra_requires=EXTRAS_REQUIRES,
    packages=find_packages(),
    py_modules=["pyDecLog"],
    classifiers=CLASSIFIERS,
)