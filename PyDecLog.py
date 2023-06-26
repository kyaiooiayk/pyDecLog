from functools import wraps, partial
import logging
import os
import time
from contextlib import redirect_stdout
from io import StringIO
import numpy as np
import inspect
from sys import getsizeof
import sys
from pympler.asizeof import asizeof


LOG_FILE_NAME = "LOG"
LOG_FILE_PATH = "./"
# It is assumed the console level will be printed only for critical component
CONSOLE_LOG_LEVEL = "critical"


def lprint(console_log_level="info"):
    """Special version of print for logging.

    Parameters
    ----------

    Returns
    -------
    """
    logger_obj = get_logger(
        log_file_name=LOG_FILE_NAME,
        log_dir=LOG_FILE_PATH,
        console_log_level=console_log_level,
    )
    return logger_obj


def _get_time(t_start, t_end, unit):
    """Get elapsed time given the unit.

    Parameters
    ----------

    Returns
    -------
    """

    if unit.lower() == "sec":
        return np.around(t_end - t_start, 3)

    elif unit.lower() == "min":
        return np.around((t_end - t_start) / 60, 3)

    elif unit.lower() == "hr":
        return np.around((t_end - t_start) / 3600, 3)
    else:
        raise TypeError(f"Unit of time {unit} not known!")


def timing(
    func_=None,
    unit="sec",
    level="debug",
    console_log_level=CONSOLE_LOG_LEVEL,
    log_file_name=LOG_FILE_NAME,
    log_file_path=LOG_FILE_PATH,
):
    """Decorate function with elapsed time.

    Parameters
    -----------

    Returns
    -------
    """

    def _decorator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            t1 = time.time()
            output = func(self, *args, **kwargs)
            t2 = time.time()

            log_level = _get_log_level(
                level, console_log_level, log_file_name, log_file_path
            )

            log_level(
                str(func.__name__)
                + " was executed in: "
                + str(_get_time(t1, t2, unit))
                + " "
                + unit
            )
            return output

        return wrapper

    if callable(func_):
        return _decorator(func_)
    elif func_ is None:
        return _decorator
    else:
        raise RuntimeWarning("Positional arguments are not supported!")


def message(
    func_=None,
    level="info",
    console_log_level=CONSOLE_LOG_LEVEL,
    log_file_name=LOG_FILE_NAME,
    log_file_path=LOG_FILE_PATH,
):
    """Control print messages.

    Takes care of both the dumped .log file
    and the console ouput. The rule used here is as follows:
    - Only general and DEBUG information are log inside the decorator.
    - Anything else is logged inside the funciton being called.

    The hierarchy is:
    LEVEL      NUMERIC VALUE
    CRITICAL : 50
    ERROR    : 40
    WARNING  : 30
    INFO     : 20
    DEBUG    : 10
    NOTSET   : 0
    """

    def _decorator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):

            s = StringIO()
            with redirect_stdout(s):
                output = func(self, *args, **kwargs)

            log_level = _get_log_level(
                level, console_log_level, log_file_name, log_file_path
            )
            for i in s.getvalue().split("\n"):
                if i:
                    log_level(i)

            return output

        return wrapper

    if callable(func_):
        return _decorator(func_)
    elif func_ is None:
        return _decorator
    else:
        raise RuntimeWarning("Positional arguments are not supported!")


def _get_log_level(level, console_log_level, log_file_name, log_file_path):
    # Create logger object
    logger_obj = get_logger(
        log_file_name=log_file_name,
        log_file_path=log_file_path,
        console_log_level=console_log_level,
    )

    if level.lower() == "info":
        log_level = logger_obj.info
    elif level.lower() == "debug":
        log_level = logger_obj.debug
    elif level.lower() == "warning":
        log_level = logger_obj.warning
    elif level.lower() == "error":
        log_level = logger_obj.error
    elif level.lower() == "critical":
        log_level = logger_obj.critical
    else:
        raise TypeError(f"Logging level {level} not known!")

    return log_level


def signature(
    func_=None,
    level="debug",
    console_log_level=CONSOLE_LOG_LEVEL,
    log_file_name=LOG_FILE_NAME,
    log_file_path=LOG_FILE_PATH,
):
    """Get function signature.

    Parameters
    ----------

    Returns
    -------
    """

    def _decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            log_level = _get_log_level(
                level, console_log_level, log_file_name, log_file_path
            )

            log_level("Method's name: " + func.__name__)
            log_level("Method's signature:" + str(inspect.signature(func)))

            # Call the function as usual
            output = func(*args, **kwargs)

            return output

        return wrapper

    if callable(func_):
        return _decorator(func_)
    elif func_ is None:
        return _decorator
    else:
        raise RuntimeWarning("Positional arguments are not supported!")


def arguments(
    func_=None,
    level="debug",
    console_log_level=CONSOLE_LOG_LEVEL,
    log_file_name=LOG_FILE_NAME,
    log_file_path=LOG_FILE_PATH,
):
    """Get args and kwargs.

    Takes care of both the dumped .log file
    and the console ouput. The rule used here is as follows:
    - Only general and DEBUG information are log inside the decorator.
    - Anything else is logged inside the funciton being called.

    The hierarchy is:
    LEVEL      NUMERIC VALUE
    CRITICAL : 50
    ERROR    : 40
    WARNING  : 30
    INFO     : 20
    DEBUG    : 10
    NOTSET   : 0
    """

    def _decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):

            log_level = _get_log_level(
                level, console_log_level, log_file_name, log_file_path
            )

            log_level("Method's name: " + func.__name__)
            log_level("Method's args: {}".format(args))
            log_level("Method's kwargs: {}".format(kwargs))

            # Call the function as usual
            output = func(*args, **kwargs)

            return output

        return wrapper

    if callable(func_):
        return _decorator(func_)
    elif func_ is None:
        return _decorator
    else:
        raise RuntimeWarning("Positional arguments are not supported!")


def description(
    func_=None, level="debug", console_log_level=CONSOLE_LOG_LEVEL
):
    """Get function description.

    Parameters
    ----------

    Returns
    -------
    """

    def _decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            log_level = _get_log_level(level, console_log_level)

            log_level("Method's description: " + func.__doc__)

            # Call the function as usual
            output = func(*args, **kwargs)

            return output

        return wrapper

    if callable(func_):
        return _decorator(func_)
    elif func_ is None:
        return _decorator
    else:
        raise RuntimeWarning("Positional arguments are not supported!")


def _get_mem(unit, value):

    if unit.lower() == "bytes":
        return asizeof(value), "bytes"
    if unit.lower() == "mb":
        return asizeof(value) / 1.0e6, "MBs"
    if unit.lower() == "gb":
        return asizeof(value) / 1.0e9, "GBs"
    if unit.lower() == "tb":
        return asizeof(value) / 1.0e12, "TBs"


def memory(
    func_=None,
    unit="bytes",
    level="debug",
    console_log_level=CONSOLE_LOG_LEVEL,
    log_file_name=LOG_FILE_NAME,
    log_file_path=LOG_FILE_PATH,
):
    """Profile local variable memory.

    Parameters
    ----------

    Returns
    -------
    """

    def _decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            log_level = _get_log_level(
                level, console_log_level, log_file_name, log_file_path
            )

            log_level(f"Function signature: {inspect.signature(func)}")

            for arg in args:
                arg_size = getsizeof(arg)
                mem_value, mem_unit = _get_mem(unit, arg_size)

                log_level(
                    f"Size of argument {str(arg)[:10]}: {mem_value} {mem_unit}"
                )

            # Check size of keyword arguments
            for key, value in kwargs.items():
                print(key, value)
                mem_value, mem_unit = _get_mem(unit, value)
                log_level(
                    f"Size of keyword argument '{str(key)[:10]}: {mem_value} {mem_unit}"
                )

            # Call the decorated function
            output = func(*args, **kwargs)

            log_level(f"Size of output: {getsizeof(output)} {mem_unit}")

            return output

        return wrapper

    if callable(func_):
        return _decorator(func_)
    elif func_ is None:
        return _decorator
    else:
        raise RuntimeWarning("Positional arguments are not supported!")


def typing(
    func_=None,
    unit="bytes",
    level="debug",
    console_log_level=CONSOLE_LOG_LEVEL,
    log_file_name=LOG_FILE_NAME,
    log_file_path=LOG_FILE_PATH,
):
    """Profile local variable type.

    Parameters
    ----------

    Returns
    -------
    """

    def _decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            log_level = _get_log_level(
                level, console_log_level, log_file_name, log_file_path
            )

            log_level(f"Function signature: {inspect.signature(func)}")

            for arg in args:
                arg_size = getsizeof(arg)
                mem_value, mem_unit = _get_mem(unit, arg_size)

                log_level(f"type of argument {type(arg)}")

            # Check size of keyword arguments
            for key, value in kwargs.items():
                print(key, value)
                mem_value, mem_unit = _get_mem(unit, value)
                log_level(f"Size of keyword argument '{type(key)}")

            # Call the decorated function
            output = func(*args, **kwargs)

            log_level(f"Type of output: {type(output)}")

            return output

        return wrapper

    if callable(func_):
        return _decorator(func_)
    elif func_ is None:
        return _decorator
    else:
        raise RuntimeWarning("Positional arguments are not supported!")


class profile_locals:
    """Profile persistent local variables."""

    def __init__(self, func):
        self._locals = {}
        self.func = func

    def __call__(self, *args, **kwargs):
        def tracer(frame, event, arg):
            if event == "return":
                self._locals = frame.f_locals.copy()

        # tracer is activated on next call, return or exception
        sys.setprofile(tracer)
        try:
            # trace the function call
            res = self.func(*args, **kwargs)
        finally:
            # disable tracer and replace with old one
            sys.setprofile(None)
        return res

    def clear_locals(self):
        self._locals = {}

    @property
    def locals(self):
        return self._locals


def get_logger(
    log_file_name="LOG",
    log_file_path=LOG_FILE_PATH,
    console_log_level=CONSOLE_LOG_LEVEL,
):
    """Creates a Log File and returns Logger object

    The hierarchy is (once set what is above is printed
    and what is below is not printed):
    LEVEL      NUMERIC VALUE
    CRITICAL : 50
    ERROR    : 40
    WARNING  : 30
    INFO     : 20
    DEBUG    : 10
    NOTSET   : 0
    """

    # Create logging folder
    if log_file_path != "./" and not os.path.exists(log_file_path):
        os.makedirs(log_file_path)

    # Build Log File Full Path
    log_path = (
        log_file_name
        if os.path.exists(log_file_name)
        else os.path.join(log_file_path, (str(log_file_name) + ".log"))
    )

    # Create handler for the log file
    # ================================
    # Create logger object and set the format for logging and other attributes
    logger = logging.Logger(log_file_name)
    # logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler(log_path, "a+")
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s %(message)s", "%Y/%m/%d | %H:%M:%S"
    )
    # ('%(asctime)s - %(levelname)-10s - %(filename)s - %(levelname)s - %(message)s'))
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # Create handler for the console output
    # ======================================
    # Define a Handler which writes INFO messages or higher to the sys.stderr
    console = logging.StreamHandler()

    # Levels are appendable
    if console_log_level.lower() == "info":
        console.setLevel(logging.INFO)
    elif console_log_level.lower() == "debug":
        console.setLevel(logging.DEBUG)
    elif console_log_level.lower() == "error":
        console.setLevel(logging.ERROR)
    elif console_log_level.lower() == "critical":
        console.setLevel(logging.CRITICAL)

    # Set a console format which is esier to read
    formatter = logging.Formatter("%(message)s")
    # tell the handler to use this format
    console.setFormatter(formatter)
    # Add the handler to the root logger
    logger.addHandler(console)

    return logger
