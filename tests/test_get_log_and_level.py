# some_name_test.py
import unittest
from unittest.mock import MagicMock
import os
import sys
import shutil
import numpy as np

sys.path.append("../")

from PyDecLog import _get_log_level
from PyDecLog import get_logger

LOG_FILE_NAME = "LOG"
LOG_FILE_PATH = "./"
CONSOLE_LOG_LEVEL = "critical"


class TestlLogger(unittest.TestCase):
    def test_get_log(self):

        logger = get_logger(
            log_file_name=LOG_FILE_NAME,
            log_file_path=LOG_FILE_PATH,
            console_log_level=CONSOLE_LOG_LEVEL,
        )

        self.assertTrue(hasattr(logger, "info"))
        self.assertTrue(hasattr(logger, "debug"))
        self.assertTrue(hasattr(logger, "warning"))
        self.assertTrue(hasattr(logger, "error"))
        self.assertTrue(hasattr(logger, "critical"))

    def test_get_log_level_error_INFO(self):

        logger = elapsed_time = _get_log_level(
            level="info",
            console_log_level=CONSOLE_LOG_LEVEL,
            log_file_name=LOG_FILE_NAME,
            log_file_path=LOG_FILE_PATH,
        )

        logger("message!")

        self.assertTrue(
            open("./LOG.log", "r").read().find("INFO message!") != -1
        )
        self.addCleanup(os.remove, "./LOG.log")

    def test_get_log_level_error_DEBUG(self):

        logger = elapsed_time = _get_log_level(
            level="debug",
            console_log_level=CONSOLE_LOG_LEVEL,
            log_file_name=LOG_FILE_NAME,
            log_file_path=LOG_FILE_PATH,
        )

        logger("message!")

        self.assertTrue(
            open("./LOG.log", "r").read().find("DEBUG message!") != -1
        )
        self.addCleanup(os.remove, "./LOG.log")

    def test_get_log_level_error_ERROR(self):

        logger = elapsed_time = _get_log_level(
            level="error",
            console_log_level=CONSOLE_LOG_LEVEL,
            log_file_name=LOG_FILE_NAME,
            log_file_path=LOG_FILE_PATH,
        )

        logger("message!")

        self.assertTrue(
            open("./LOG.log", "r").read().find("ERROR message!") != -1
        )
        self.addCleanup(os.remove, "./LOG.log")

    def test_get_log_level_error_CRITICAL(self):

        logger = elapsed_time = _get_log_level(
            level="critical",
            console_log_level=CONSOLE_LOG_LEVEL,
            log_file_name=LOG_FILE_NAME,
            log_file_path=LOG_FILE_PATH,
        )

        logger("message!")

        self.assertTrue(
            open("./LOG.log", "r").read().find("CRITICAL message!") != -1
        )
        self.addCleanup(os.remove, "./LOG.log")

    def test_get_log_console_level_INFO(self):

        logger = elapsed_time = _get_log_level(
            level="critical",
            console_log_level="info",
            log_file_name=LOG_FILE_NAME,
            log_file_path=LOG_FILE_PATH,
        )

        logger("message!")

        self.assertTrue(
            open("./LOG.log", "r").read().find("CRITICAL message!") != -1
        )
        self.addCleanup(os.remove, "./LOG.log")

    def test_get_log_console_level_DEBUG(self):

        logger = elapsed_time = _get_log_level(
            level="critical",
            console_log_level="debug",
            log_file_name=LOG_FILE_NAME,
            log_file_path=LOG_FILE_PATH,
        )

        logger("message!")

        self.assertTrue(
            open("./LOG.log", "r").read().find("CRITICAL message!") != -1
        )
        self.addCleanup(os.remove, "./LOG.log")

    def test_get_log_console_level_ERROR(self):

        logger = elapsed_time = _get_log_level(
            level="critical",
            console_log_level="error",
            log_file_name=LOG_FILE_NAME,
            log_file_path=LOG_FILE_PATH,
        )

        logger("message!")

        self.assertTrue(
            open("./LOG.log", "r").read().find("CRITICAL message!") != -1
        )
        self.addCleanup(os.remove, "./LOG.log")

    def test_raise_type_error(self):

        with self.assertRaises(TypeError):
            logger = elapsed_time = _get_log_level(
                level="disaster",
                console_log_level=CONSOLE_LOG_LEVEL,
                log_file_name=LOG_FILE_NAME,
                log_file_path=LOG_FILE_PATH,
            )


if __name__ == "__main__":
    unittest.main()
