import functools
import itertools
import logging
import os
import shutil

import time
from contextlib import redirect_stdout
from io import StringIO
import numpy as np
import inspect

LOG_FILE_NAME = "LOG"
LOG_FILE_DIR = "./"
# It is assume the console level will be printed only for critical component
CONSOLE_LOG_LEVEL = "critical"


def lprint(console_log_level="info"):
    logger_obj = get_logger(
        log_file_name=LOG_FILE_NAME,
        log_dir=LOG_FILE_DIR,
        console_log_level=console_log_level,
    )
    return logger_obj


def _get_time(t_start, t_end, unit):
    if unit.lower() == "sec":
        return np.around(t_end - t_start, 3)

    elif unit.lower() == "min":
        return np.around((t_end - t_start) / 60, 3)

    elif unit.lower() == "hr":
        return np.around((t_end - t_start) / 3600, 3)


def timing(unit="sec", level="debug", console_log_level=CONSOLE_LOG_LEVEL):
    """Timer decorator
    Time the execution time of the passed in function.
    """

    def decorator(func):
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            t1 = time.time()
            result = func(self, *args, **kwargs)
            t2 = time.time()

            log_level = _get_log_level(level, console_log_level=console_log_level)

            log_level(
                str(func.__name__)
                + " was executed in: "
                + str(_get_time(t1, t2, unit))
                + unit
            )
            return result

        return wrapper

    return decorator


def message(level="info", console_log_level=CONSOLE_LOG_LEVEL):
    """Control print messages

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

    def decorator(func):
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            logger_obj = get_logger(log_file_name=LOG_FILE_NAME, log_dir=LOG_FILE_DIR)

            s = StringIO()
            with redirect_stdout(s):
                result = func(self, *args, **kwargs)

            log_level = _get_log_level(level, console_log_level=console_log_level)
            for i in s.getvalue().split("\n"):
                if i:
                    log_level(i)

            return result

        return wrapper

    return decorator


def _get_log_level(level, console_log_level):
    # Create logger object
    logger_obj = get_logger(
        log_file_name=LOG_FILE_NAME,
        log_dir=LOG_FILE_DIR,
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


def signature(level="debug", console_log_level=CONSOLE_LOG_LEVEL):
    """Fwt function signature"""

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            log_level = _get_log_level(level, console_log_level)

            log_level("Method's name: " + func.__name__)
            log_level("Method's singature:" + str(inspect.signature(func)))

            # Call the function as usual
            value = func(*args, **kwargs)

            return value

        return wrapper

    return decorator


def arguments(level="debug", console_log_level=CONSOLE_LOG_LEVEL):
    """Control print messages

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

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            log_level = _get_log_level(level, console_log_level)

            log_level("Method's name: " + func.__name__)
            log_level("Method's args: {}".format(args))
            log_level("Method's kwargs: {}".format(kwargs))

            # Call the function as usual
            value = func(*args, **kwargs)

            return value

        return wrapper

    return decorator


def get_logger(
    log_file_name="LOG", log_dir=LOG_FILE_DIR, console_log_level=CONSOLE_LOG_LEVEL
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

    # Build Log File Full Path
    logPath = (
        log_file_name
        if os.path.exists(log_file_name)
        else os.path.join(log_dir, (str(log_file_name) + ".log"))
    )

    # Create handler for the log file
    # ================================
    # Create logger object and set the format for logging and other attributes
    logger = logging.Logger(log_file_name)
    # logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler(logPath, "a+")
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

    # Return logger object
    return logger