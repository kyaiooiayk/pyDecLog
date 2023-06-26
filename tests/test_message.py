# some_name_test.py
import unittest
from unittest.mock import MagicMock
import os
import sys
import shutil

sys.path.append("../")

from PyDecLog import message as mes


class TestMessage(unittest.TestCase):
    def test_same_function_return(self):
        @mes
        def dummy(x):
            return x

        self.assertTrue(dummy(1), 1)
        self.addCleanup(os.remove, "./LOG.log")

    def test_log_file_exhists(self):
        @mes
        def dummy(x):
            return x

        dummy(1)
        self.assertTrue(os.path.exists("./LOG.log"))
        self.addCleanup(os.remove, "./LOG.log")

    def test_log_file_not_empty(self):
        @mes
        def dummy(x):
            print("Testing message!")
            return x

        dummy(1)
        self.assertFalse(os.stat("./LOG.log").st_size == 0)
        self.addCleanup(os.remove, "./LOG.log")

    def test_log_file_content_for_message_string(self):
        @mes
        def dummy(x):
            print("Testing message!")
            return x

        dummy(1)
        self.assertTrue(
            open("./LOG.log", "r").read().find("INFO Testing message!") != -1
        )
        self.addCleanup(os.remove, "./LOG.log")

    def test_log_CRITICAL_file(self):
        @mes(level="critical")
        def dummy(x):
            print("Testing message!")
            return x

        dummy(1)
        self.assertTrue(
            open("./LOG.log", "r").read().find("CRITICAL Testing message!")
            != -1
        )
        self.addCleanup(os.remove, "./LOG.log")

    def test_log_INFO_file(self):
        @mes(level="info")
        def dummy(x):
            print("Testing message!")
            return x

        dummy(1)
        self.assertTrue(
            open("./LOG.log", "r").read().find("INFO Testing message!") != -1
        )
        self.addCleanup(os.remove, "./LOG.log")

    def test_log_DEBUG_file(self):
        @mes(level="debug")
        def dummy(x):
            print("Testing message!")
            return x

        dummy(1)
        self.assertTrue(
            open("./LOG.log", "r").read().find("DEBUG Testing message!") != -1
        )
        self.addCleanup(os.remove, "./LOG.log")

    def test_log_ERROR_file(self):
        @mes(level="error")
        def dummy(x):
            print("Testing message!")
            return x

        dummy(1)
        self.assertTrue(
            open("./LOG.log", "r").read().find("ERROR Testing message!") != -1
        )
        self.addCleanup(os.remove, "./LOG.log")

    def test_log_WARNING_file(self):
        @mes(level="warning")
        def dummy(x):
            print("Testing message!")
            return x

        dummy(1)
        self.assertTrue(
            open("./LOG.log", "r").read().find("WARNING Testing message!")
            != -1
        )
        self.addCleanup(os.remove, "./LOG.log")

    def test_log_name_file_change(self):
        @mes(log_file_name="test")
        def dummy(x):
            print("Testing message!")
            return x

        dummy(1)
        self.assertTrue(os.path.exists("./test.log"))
        self.addCleanup(os.remove, "./test.log")

    def test_log_path_file_change(self):
        @mes(log_file_path="test_log_folder")
        def dummy(x):
            print("Testing message!")
            return x

        dummy(1)
        self.assertTrue(os.path.exists("./test_log_folder/LOG.log"))
        self.addCleanup(shutil.rmtree, "./test_log_folder")

    def test_raise_run_time_warning(self):

        with self.assertRaises(RuntimeWarning):

            @mes("test_log_folder")
            def dummy(x):
                return x


if __name__ == "__main__":
    unittest.main()
