import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

VERSION = "0.1.3"
PACKAGE_NAME = "pyDecLog"
AUTHOR = "kyaiooiayk"
AUTHOR_EMAIL = "kayaiooiayk@email.com"
URL = "https://github.com/kyaiooiayk/pyDecLog"

LICENSE = "MIT"
DESCRIPTION = "pyDecLog: a python package for logging via decorators "
LONG_DESCRIPTION = (HERE / "README.md").read_text()
LONG_DESC_TYPE = "text/markdown"

INSTALL_REQUIRES = ["pympler", "numpy"]

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
    install_requires=INSTALL_REQUIRES,
    packages=find_packages(),
    py_modules=["pyDecLog"]
)