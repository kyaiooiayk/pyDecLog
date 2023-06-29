from pyDecLog import arguments as args
import unittest
from unittest.mock import MagicMock
import os
import sys
import shutil


class TestArguments(unittest.TestCase):
    def test_same_function_return(self):
        @args
        def dummy(x):
            return x

        self.assertTrue(dummy(1), 1)
        self.addCleanup(os.remove, "./LOG.log")

    def test_log_file_exhists(self):
        @args
        def dummy(x):
            return x

        dummy(1)
        self.assertTrue(os.path.exists("./LOG.log"))
        self.addCleanup(os.remove, "./LOG.log")

    def test_log_file_not_empty(self):
        @args
        def dummy(x):
            print("Testing message!")
            return x

        dummy(1)
        self.assertFalse(os.stat("./LOG.log").st_size == 0)
        self.addCleanup(os.remove, "./LOG.log")

    def test_log_file_content_for_argument_string(self):
        @args
        def dummy(x):
            return x

        dummy(1)
        self.assertTrue(
            open("./LOG.log", "r").read().find("Method's args:") != -1
        )
        self.assertTrue(
            open("./LOG.log", "r").read().find("Method's kwargs:") != -1
        )
        self.addCleanup(os.remove, "./LOG.log")

    def test_log_CRITICAL_file(self):
        @args(level="critical")
        def dummy(x):
            return x

        dummy(1)
        self.assertTrue(
            open("./LOG.log", "r").read().find("CRITICAL Method's args:") != -1
        )
        self.assertTrue(
            open("./LOG.log", "r").read().find("CRITICAL Method's kwargs:")
            != -1
        )
        self.addCleanup(os.remove, "./LOG.log")

    def test_log_INFO_file(self):
        @args(level="info")
        def dummy(x):
            print("Testing message!")
            return x

        dummy(1)
        self.assertTrue(
            open("./LOG.log", "r").read().find("INFO Method's args:") != -1
        )
        self.assertTrue(
            open("./LOG.log", "r").read().find("INFO Method's kwargs:") != -1
        )
        self.addCleanup(os.remove, "./LOG.log")

    def test_log_DEBUG_file(self):
        @args(level="debug")
        def dummy(x):
            print("Testing message!")
            return x

        dummy(1)
        self.assertTrue(
            open("./LOG.log", "r").read().find("DEBUG Method's args:") != -1
        )
        self.assertTrue(
            open("./LOG.log", "r").read().find("DEBUG Method's kwargs:") != -1
        )
        self.addCleanup(os.remove, "./LOG.log")

    def test_log_ERROR_file(self):
        @args(level="error")
        def dummy(x):
            print("Testing message!")
            return x

        dummy(1)

        self.assertTrue(
            open("./LOG.log", "r").read().find("ERROR Method's args:") != -1
        )
        self.assertTrue(
            open("./LOG.log", "r").read().find("ERROR Method's kwargs:") != -1
        )

        self.addCleanup(os.remove, "./LOG.log")

    def test_log_WARNING_file(self):
        @args(level="warning")
        def dummy(x):
            print("Testing message!")
            return x

        dummy(1)

        self.assertTrue(
            open("./LOG.log", "r").read().find("WARNING Method's args:") != -1
        )
        self.assertTrue(
            open("./LOG.log", "r").read().find("WARNING Method's kwargs:")
            != -1
        )
        self.addCleanup(os.remove, "./LOG.log")

    def test_log_name_file_change(self):
        @args(log_file_name="test")
        def dummy(x):
            return x

        dummy(1)
        self.assertTrue(os.path.exists("./test.log"))
        self.addCleanup(os.remove, "./test.log")

    def test_log_path_file_change(self):
        @args(log_file_path="test_log_folder")
        def dummy(x):
            return x

        dummy(1)
        self.assertTrue(os.path.exists("./test_log_folder/LOG.log"))
        self.addCleanup(shutil.rmtree, "./test_log_folder")

    def test_raise_run_time_warning(self):

        with self.assertRaises(RuntimeWarning):

            @args("test_log_folder")
            def dummy(x):
                return x


if __name__ == "__main__":
    unittest.main()
