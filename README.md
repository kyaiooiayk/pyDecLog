# pyDecLog

![PyPI Version](https://img.shields.io/pypi/v/pyDecLog.svg)
![Python Version](https://img.shields.io/pypi/pyversions/pyDecLog.svg)
![PyPI - Downloads](https://img.shields.io/pypi/dm/pyDecLog)
[![HitCount](https://hits.dwyl.com/kyaiooiayk/pyDecLog.svg)](https://hits.dwyl.com/kyaiooiayk/pyDecLog)
![License](https://img.shields.io/pypi/l/pyDecLog)
![Stars](https://img.shields.io/github/stars/kyaiooiayk/pyDecLog)
![Issues](https://img.shields.io/github/issues/kyaiooiayk/pyDecLog)
![Forks](https://img.shields.io/github/forks/kyaiooiayk/pyDecLog)
[![codecov](https://codecov.io/gh/kyaiooiayk/pyDecLog/branch/main/graph/badge.svg?token=FU80PXXRRI)](https://codecov.io/gh/kyaiooiayk/pyDecLog)

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

pyDecLog: a simple and easy to use Python module for logging via decorators.
***

## 🚀Quick start
- Say we have the following workflow
```python
from pyDecLog import arguments
from pyDecLog import signature
from pyDecLog import message
from pyDecLog import timing
from pyDecLog import lprint
from pyDecLog import description
import time

def workflow():

    # Set console level to the same level of the message level so it is shown in the console
    lprint(console_log_level="info").info("Workflow starts!")

    # Decorate function as needed
    @doscription
    @signature
    @arguments
    @timing
    @message
    def sum_two_int(first, second=2):
        """Sum two numbers."""

        print("Some message on console")
        result = first + second
        time.sleep(2)
        print("Result is: " + str(result))
        return result

    sum_tow_int(1, 1)

    # Set console level to the same level of the message so it is shown in the console
    lprint(console_log_level="info").info("Workflow ends!")


if __name__ == "__main__":
    workflow()
```
- Upon execution the following is printed on console:
```shell
Workflow starts!
Workflow ends!
```
- Upon execution a `LOG.log` file is written:
```shell
2023/06/24 | 18:20:50 | ERROR Workflow starts!
2023/06/24 | 18:20:50 | DEBUG Method's description: Sum two numbers.
2023/06/24 | 18:20:50 | DEBUG Method's name: sum_
2023/06/24 | 18:20:50 | DEBUG Method's signature:(first, second=2)
2023/06/24 | 18:20:50 | DEBUG Method's name: sum_
2023/06/24 | 18:20:50 | DEBUG Method's args: (1, 1)
2023/06/24 | 18:20:50 | DEBUG Method's kwargs: {}
2023/06/24 | 18:20:52 | INFO Some message on console
2023/06/24 | 18:20:52 | INFO Result is: 2
2023/06/24 | 18:20:52 | DEBUG sum_ was executed in: 2.006 sec
2023/06/24 | 18:20:52 | ERROR Workflow ends!
```

## 🚀Useful for
- Keep track of Python pipelines.
- Log info about a function during development both via Python script or Jupyter Notebook.
***

## ⚙️Installation
- Create your own virtual environment and run `pip install -r requirements.txt`
- Via pip: `pip install pyDecLog`
***

## 🔗Dependencies
- PyDevLog requires Python 3.5 or higher, and the following packages:
  - `pympler`
  - `numpy`
***

## 🧑‍🤝‍🧑Contributions
- All contributions (bug, suggestion, new feature) are welcome.
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

## ⚠️Known issues
- `@profile_locals` does not write to the log file. Its output needs to be piped separately to the LOG.log file. See the following example:
```python
from pyDecLog import profile_locals as profile
from pyDecLog import lprint
from pympler.asizeof import asizeof

@profile
def func(x):
    local_1 = 1
    local_2 = 2
    return 1

func()

for key, value in func.locals.items():
    msg = f"Variable: {key} | value: {value} | type: {type(value)} | size: {asizeof(value)}"

    lprint(console_log_level="debug").debug(msg)
```
- The following `LOG.log` is the written:
```shell
2023/06/28 | 07:04:52 | DEBUG Variable: x | value: 1 | type: <class 'int'> | size: 32
2023/06/28 | 07:04:52 | DEBUG Variable: local_1 | value: 1 | type: <class 'int'> | size: 32
2023/06/28 | 07:04:52 | DEBUG Variable: local_2 | value: 2 | type: <class 'int'> | size: 32
```
***

## 📚Tutorials
- See the `examples` folder.
***

## 📚References
- [Decorators with parameters?](https://stackoverflow.com/questions/5929107/decorators-with-parameters)
- [How to expose persistent local variables? Part#1](https://code.activestate.com/recipes/577283-decorator-to-expose-local-variables-of-a-function-/)
- [How to expose persistent local variables? Part#2](https://stackoverflow.com/questions/9186395/python-is-there-a-way-to-get-a-local-function-variable-from-within-a-decorator)
- [How to time your code](https://stackoverflow.com/questions/17579357/time-time-vs-timeit-timeit)
***

## 📝Changelog
- `0.1.6` - First release (26/06/23).
- `0.1.7` - Added `@machine` and  `@user` (29/06/23).
***

## 📝To-do
- There is no planned development.
***

## 🪪License
- MIT License
***

## Developers
- Doc string were generated via [autoDocstring](https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring) package using NumPy format style.
- Typing hints for function return type by [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance).
- Testing was done via unittesting.
***
