# pyDecLog
PyDecLog: a simple and easy to use Python package for logging via decorators.
***

## 🚀Quick start
- Say we have the following workflow
```
```

## 🚀Useful for
- Keep track of Python pipelines.
- Log info about a function during development both on python script or jupyter notebook.
***

## ⚙️Installation
- Create your own virtual environment and run `pip install -r requirements.txt`, then choose one of the following options:
  - Option 1, via pip: `pip install pydeclog`
  - Option 2, via conda package manager: `conda install -c conda-forge pydeclog`
  - Option 3, from source: `pip install git+https://github.com/kayaiooiayk/pydeclog.git`
***

## 🔗Dependencies
- PyDevLog requires Python 3.5 or higher, and the following packages:
  - `pympler`
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
- `@profile_local`: log function's local persistent variables and add an attribute to the function.
***

## 🪄Features
- Mix and match the decorators you want.
- Can control logging levels.
- Can control where logging messages are piped: to log file or both log file and console.
- Can add comments directly to log file even outside a function.
***

## ⚠️Known issues
- `@profile_local` does not write to the log file. Its output needs to be piped separately to the log. See the following example:
```python
```
***

## 📚Tutorials
- See the `example` folder.
***

## 📚References
- [Decorators with parameters?](https://stackoverflow.com/questions/5929107/decorators-with-parameters)
- [How to expose persistent local variables? Part#1](https://code.activestate.com/recipes/577283-decorator-to-expose-local-variables-of-a-function-/)
- [How to expose persistent local variables? Part#2](https://stackoverflow.com/questions/9186395/python-is-there-a-way-to-get-a-local-function-variable-from-within-a-decorator)
***

## 📝Changelog
- `0.1.0`  fist release (30/06/23).
- ***

## 📝To-do
- There is no planned development.
***

## 🪪License
- MIT License
***
