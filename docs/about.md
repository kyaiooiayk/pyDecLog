# pyDecLog

![PyPI Version](https://img.shields.io/pypi/v/pyDecLog.svg)
![Python Version](https://img.shields.io/pypi/pyversions/pyDecLog.svg)
![PyPI - Downloads](https://img.shields.io/pypi/dm/pyDecLog)
[![HitCount](https://hits.dwyl.com/kyaiooiayk/pyDecLog.svg)](https://hits.dwyl.com/kyaiooiayk/pyDecLog)
![License](https://img.shields.io/pypi/l/pyDecLog)
![Stars](https://img.shields.io/github/stars/kyaiooiayk/pyDecLog)
![Issues](https://img.shields.io/github/issues/kyaiooiayk/pyDecLog)
![Forks](https://img.shields.io/github/forks/kyaiooiayk/pyDecLog)
[![codecov](https://codecov.io/gh/kyaiooiayk/pyDecLog/branch/main/graph/badge.svg?token=H28KHYYFHX)](https://codecov.io/gh/kyaiooiayk/pyDecLog)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

pyDecLog: a simple and easy to use Python module for logging via decorators.
***


## 🚀Useful for
- Keep track of Python pipelines.
- Log info about a function during development both via Python script or Jupyter Notebook.
***

## 🎨Available decorators
- `@arguments`: log function's args and kwargs
- `@comment`: log all function's inner print statements
- `@description`: log function's output from the `__doc__` dunder method
- `@machine`: log machine OS system and hardware
- `@memory`: log function's args, kwargs and output memory usage
- `@message`: log function's print statements
- `@profile_locals`: log function's local persistent variables
- `@signature`: log function's signature
- `@timing`: log function's elapsed time
- `@typing`: log function's args, kwargs and output type
- `@user`: log user info
***

## 🪄Features
- Mix and match the decorators you want.
- Can control logging levels as a whole or individually. Choose from the following:
    - `CRITICAL`
    - `ERROR`
    - `WARNING`
    - `INFO`
    - `DEBUG`
- Can control where logging messages are piped: to log file or both log file and console. When controlling the message at the console level the following hierarchy is enforced:
```
CRITICAL : 50
ERROR    : 40
WARNING  : 30
INFO     : 20
DEBUG    : 10
NOTSET   : 0
```
- Can add comments directly to log file even outside a function.
***
