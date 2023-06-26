from pyDecLog import message as mes
from pyDecLog import lprint
import unittest
from unittest.mock import MagicMock
import os
import sys
import shutil


class TestlPrint(unittest.TestCase):
    def test_log_file_exhists(self):

        lprint(console_log_level="info").info("simple message")

        self.assertTrue(os.path.exists("./LOG.log"))
        self.addCleanup(os.remove, "./LOG.log")

    def test_log_file_not_empty(self):

        lprint(console_log_level="info").info("simple message")

        self.assertFalse(os.stat("./LOG.log").st_size == 0)
        self.addCleanup(os.remove, "./LOG.log")

    def test_log_CRITICAL_file(self):

        lprint(console_log_level="info").critical("simple message")

        self.assertTrue(open("./LOG.log", "r").read().find("CRITICAL") != -1)
        self.addCleanup(os.remove, "./LOG.log")

    def test_log_INFO_file(self):

        lprint(console_log_level="info").info("simple message")
        self.assertTrue(open("./LOG.log", "r").read().find("INFO") != -1)
        self.addCleanup(os.remove, "./LOG.log")

    def test_log_DEBUG_file(self):

        lprint(console_log_level="info").debug("simple message")
        self.assertTrue(open("./LOG.log", "r").read().find("DEBUG") != -1)
        self.addCleanup(os.remove, "./LOG.log")

    def test_log_ERROR_file(self):

        lprint(console_log_level="info").error("simple message")

        self.assertTrue(open("./LOG.log", "r").read().find("ERROR") != -1)
        self.addCleanup(os.remove, "./LOG.log")

    def test_log_WARNING_file(self):
        lprint(console_log_level="info").warning("simple message")

        self.assertTrue(open("./LOG.log", "r").read().find("WARNING") != -1)
        self.addCleanup(os.remove, "./LOG.log")

    def test_log_name_file_change(self):

        lprint(console_log_level="info", log_file_name="test").warning(
            "simple message"
        )
        self.assertTrue(os.path.exists("./test.log"))
        self.addCleanup(os.remove, "./test.log")

    def test_log_path_file_change(self):
        lprint(
            console_log_level="info", log_file_path="test_log_folder"
        ).warning("simple message")
        self.assertTrue(os.path.exists("./test_log_folder/LOG.log"))
        self.addCleanup(shutil.rmtree, "./test_log_folder")


if __name__ == "__main__":
    unittest.main()
