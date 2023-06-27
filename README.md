# pyDecLog

![PyPI Version](https://img.shields.io/pypi/v/pyDecLog.svg)
![Python Version](https://img.shields.io/pypi/pyversions/pyDecLog.svg)
![PyPI - Downloads](https://img.shields.io/pypi/dm/pyDecLog)
![License](https://img.shields.io/pypi/l/pyDecLog)
![Stars](https://img.shields.io/github/stars/SnowballSH/pyDecLog)
![Issues](https://img.shields.io/github/issues/SnowballSH/pyDecLog)
![Forks](https://img.shields.io/github/forks/SnowballSH/pyDecLog)

pyDecLog: a simple and easy to use Python module for logging via decorators.
***

## 🚀Quick start
- Say we have the following workflow
```python
from pyDecLog import arguments as arg
from pyDecLog import signature as sign
from pyDecLog import message as mes
from pyDecLog import timing as tim
from pyDecLog import lprint
from pyDecLog import description as doc
from pyDecLog import memory as mem
import time
import sys

def workflow():

    # Set console level to the same level of the message level so it is shown in the console
    lprint(console_log_level="info").info("Workflow starts!")

    # Decorate function as needed
    @doc
    @sign
    @arg
    @tim
    @mes
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
- Upin execution the following is printed on console:
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
- Log info about a function during development both on python script or jupyter notebook.
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
- `@comment`: log all the print statements inside a decorated function
- `@timing`: log the function elapsed time
- `@signature`: log function's signature
- `@arguments`: log function's args and kwargs
- `@message`: log the function's print statements
- `@typing`: log function's args, kwargs and output type
- `@memory`: log function's args, kwargs and output their memory usage
- `@description`: log function's output from the `__doc__` dunder method
- `@profile_local`: log function's local persistent variables.
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
- `@profile_locals` does not write to the log file. Its output needs to be piped separately to the log. See the following example:
```python
from pyDecLog import profile_locals as profile
from pyDecLog import lprint

@profile
def func():
    local1 = 1
    local2 = 2
    return 1

func()

for key, value in func.locals.items():
    msg = f"Variable: {key} | value: {value} | type: {type(value)} | size: {asizeof(value)}"

    lprint(console_log_level="debug").debug(msg)
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
- `0.1.4`  first release (26/06/23).
***

## 📝To-do
- There is no planned development.
***

## 🪪License
- MIT License
***

## Developers
- Doc string were generated via [autoDocstring](https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring) package using NumPy fomrat.
- Typing hints for function return type by [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance).
- Testing was done via unittesting.
***
