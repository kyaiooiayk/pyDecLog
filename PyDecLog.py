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
CONSOLE_LOG_LEVEL = "critical"


def lprint(
    console_log_level: str = CONSOLE_LOG_LEVEL,
    log_file_name: str = LOG_FILE_NAME,
    log_file_path: str = LOG_FILE_PATH,
):
    """Log print (lprint).

    Parameters
    ----------
    console_log_level : str, optional
        Set console log level, by default CONSOLE_LOG_LEVEL
    log_file_name : str, optional
        Log file name, by default LOG_FILE_NAME
    log_file_path : str, optional
        Set log file path, by default LOG_FILE_PATH

    Returns
    -------
    object
        Logger object
    """

    logger_obj = get_logger(
        log_file_name=log_file_name,
        console_log_level=console_log_level,
        log_file_path=log_file_path,
    )
    return logger_obj


def _get_time(t_start: float, t_end: float, unit: str):
    """Get elapsed time given the unit.

    Parameters
    ----------
    t_start : float
        kernel time at start of process.
    t_end : float
        Kernel time at end of process.
    unit : str
        String describing unit of time: sec, min or hr.

    Returns
    -------
    float
        Elapsed time.

    Raises
    ------
    TypeError
        Raise of the unit is not known.
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
    func_: None = None,
    unit: str = "sec",
    level: str = "debug",
    console_log_level: str = CONSOLE_LOG_LEVEL,
    log_file_name: str = LOG_FILE_NAME,
    log_file_path: str = LOG_FILE_PATH,
):
    """Wrap function with execution time.

    Parameters
    ----------
    func_ : None, optional
        Wrapped function, by default None.
    unit : str, optional
        Unit of time: "sec", "min" or "hr", by default "sec".
    level : str, optional
        Log level: "debug", "info", "critical" or "error", by default "debug".
    console_log_level : str, optional
        Console log level. Same options as log level, by default CONSOLE_LOG_LEVEL.
    log_file_name : str, optional
        Name of the log file, by default LOG_FILE_NAME.
    log_file_path : str, optional
        Path of the log file, by default LOG_FILE_PATH.

    Raises
    ------
    RunTimeWarning
        Raise if called with positional arguments.
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
                f"{str(func.__name__)} was executed in: {str(_get_time(t1, t2, unit))} {unit}"
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
    func_: None = None,
    level: str = "info",
    console_log_level: str = CONSOLE_LOG_LEVEL,
    log_file_name: str = LOG_FILE_NAME,
    log_file_path: str = LOG_FILE_PATH,
):
    """Collect and pip all functions calls.

    Parameters
    ----------
    func_ : None, optional
        Wrapped function, by default None.
    level : str, optional
        Log level: "debug", "info", "critical" or "error", by default "debug"
    console_log_level : str, optional
        Console log level. Same options as log level, by default CONSOLE_LOG_LEVEL.
    log_file_name : str, optional
        Name of the log file, by default LOG_FILE_NAME.
    log_file_path : str, optional
        Path of the log file, by default LOG_FILE_PATH.

    Raises
    ------
    RunTimeWarning
        Raise if called with positional arguments.
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


def _get_log_level(
    level: str, console_log_level: str, log_file_name: str, log_file_path: str
):
    """Return Logger object given a log level.

    Parameters
    ----------
    level : str
        Log level: "debug", "info", "critical" or "error".
    console_log_level : str
        Console log level.
    log_file_name : str
        Name of the log file.
    log_file_path : str
        Path of the log file

    Returns
    -------
    Obejct
        Logger

    Raises
    ------
    TypeError
        Raised of logging level is not known.
    """

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
    func_: None = None,
    level: str = "debug",
    console_log_level: str = CONSOLE_LOG_LEVEL,
    log_file_name: str = LOG_FILE_NAME,
    log_file_path: str = LOG_FILE_PATH,
):
    """Get function signature.

    Parameters
    ----------
    func_ : None, optional
        Wrapped function, by default None.
    level : str, optional
        Log level: "debug", "info", "critical" or "error", by default "debug".
    console_log_level : str, optional
        Console log level. Same options as log level, by default CONSOLE_LOG_LEVEL.
    log_file_name : str, optional
        Name of the log file, by default LOG_FILE_NAME.
    log_file_path : str, optional
        Path of the log file, by default LOG_FILE_PATH.
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
    func_: None = None,
    level: str = "debug",
    console_log_level: str = CONSOLE_LOG_LEVEL,
    log_file_name: str = LOG_FILE_NAME,
    log_file_path: str = LOG_FILE_PATH,
):
    """Get args and kwargs.

    Parameters
    ----------
    func_ : None, optional
        Wrapped function, by default None.
    level : str, optional
        Log level: "debug", "info", "critical" or "error", by default "debug".
    console_log_level : str, optional
        Console log level. Same options as log level,
        by default CONSOLE_LOG_LEVEL.
    log_file_name : str, optional
        Name of the log file, by default LOG_FILE_NAME.
    log_file_path : str, optional
        Path of the log file, by default LOG_FILE_PATH.
    """

    def _decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):

            log_level = _get_log_level(
                level, console_log_level, log_file_name, log_file_path
            )

            log_level(f"Method's name: {func.__name__}")
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
    func_: None = None,
    level: str = "debug",
    console_log_level: str = CONSOLE_LOG_LEVEL,
    log_file_name: str = LOG_FILE_NAME,
    log_file_path: str = LOG_FILE_PATH,
):
    """Describe function by pulling __doc__ string.

    Parameters
    ----------
    func_ : None, optional
        _description_, by default None
    level : str, optional
        Log level: "debug", "info", "critical" or "error", by default "debug".
    console_log_level : str, optional
        Console log level. Same options as log level,
        by default CONSOLE_LOG_LEVEL.
    log_file_name : str, optional
        Name of the log file, by default LOG_FILE_NAME.
    log_file_path : str, optional
        Path of the log file, by default LOG_FILE_PATH.

    Raises
    ------
    RunTimeWarning
        Raised if positional argument is used.
    """

    def _decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            log_level = _get_log_level(
                level, console_log_level, log_file_name, log_file_path
            )

            log_level(f"Method's description: {func.__doc__}")

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


def _get_mem(unit: str, value: float):
    """Get memory formatting given the unit.

    Parameters
    ----------
    unit : str
        Unit of memory: "bytes", "mb", "gb" or "tb".
    value : float
        Amount of memory used.

    Returns
    -------
    float
        Amount of memory used in the chosen unit.
    """

    if unit.lower() == "bytes":
        return asizeof(value), "bytes"
    if unit.lower() == "mb":
        return asizeof(value) / 1.0e6, "MBs"
    if unit.lower() == "gb":
        return asizeof(value) / 1.0e9, "GBs"
    if unit.lower() == "tb":
        return asizeof(value) / 1.0e12, "TBs"


def memory(
    func_: None = None,
    unit: str = "bytes",
    level: str = "debug",
    console_log_level: str = CONSOLE_LOG_LEVEL,
    log_file_name: str = LOG_FILE_NAME,
    log_file_path: str = LOG_FILE_PATH,
):
    """Profile local variables memory.

    Parameters
    ----------
    func_ : None, optional
        Wrapped function, by default None
    unit : str, optional
        Unit of memory: "bytes", "mb", "gb" or "tr", by default "bytes"
    level : str, optional
        Log level: "debug", "info", "critical" or "error", by default "debug"
    console_log_level : str, optional
        Console log level. Same options as log level, by default CONSOLE_LOG_LEVEL.
    log_file_name : str, optional
        Name of the log file, by default LOG_FILE_NAME.
    log_file_path : str, optional
        Path of the log file, by default LOG_FILE_PATH.

    Raises
    ------
    RunTimeWarning
        Raise if called with positional arguments.
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
    func_: None = None,
    unit: str = "bytes",
    level: str = "debug",
    console_log_level: str = CONSOLE_LOG_LEVEL,
    log_file_name: str = LOG_FILE_NAME,
    log_file_path: str = LOG_FILE_PATH,
):
    """Profile local variable type.

    Parameters
    ----------
    func_ : None, optional
        Wrapped function, by default None
    unit : str, optional
        Unit of memory: "bytes", "mb", "gb" or "tr", by default "bytes"
    level : str, optional
        Log level: "debug", "info", "critical" or "error", by default "debug"
    console_log_level : str, optional
        Console log level. Same options as log level, by default CONSOLE_LOG_LEVEL.
    log_file_name : str, optional
        Name of the log file, by default LOG_FILE_NAME.
    log_file_path : str, optional
        Path of the log file, by default LOG_FILE_PATH.

    Raises
    ------
    RunTimeWarning
        Raise if called with positional arguments.
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

        # Tracer is activated on next call, return or exception
        sys.setprofile(tracer)
        try:
            # Trace the function call
            res = self.func(*args, **kwargs)
        finally:
            # Disable tracer and replace with old one
            sys.setprofile(None)
        return res

    def clear_locals(self):
        self._locals = {}

    @property
    def locals(self):
        return self._locals


def get_logger(
    log_file_name: str = LOG_FILE_NAME,
    log_file_path: str = LOG_FILE_PATH,
    console_log_level: str = CONSOLE_LOG_LEVEL,
):
    """Creates a Log File and returns Logger object.

    Parameters
    ----------
    log_file_name : str, optional
        Name of the log file, by default LOG_FILE_NAME.
    log_file_path : str, optional
        Path of the log file, by default LOG_FILE_PATH.
    console_log_level : str, optional
        Console log level. Same options as log level, by default CONSOLE_LOG_LEVEL.

    Returns
    -------
    object
        Logger object.
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
    logger = logging.Logger(log_file_name)
    handler = logging.FileHandler(log_path, "a+")
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s %(message)s", "%Y/%m/%d | %H:%M:%S"
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # Create handler for the console output
    console = logging.StreamHandler()

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
    # Tell the handler to use this format
    console.setFormatter(formatter)
    # Add the handler to the root logger
    logger.addHandler(console)

    return logger
