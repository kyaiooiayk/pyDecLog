# some_name_test.py
import unittest
from unittest.mock import MagicMock
import os
import sys
import shutil

sys.path.append("../")

from PyDecLog import memory as mem


class TestTiming(unittest.TestCase):
    def test_same_function_return(self):
        @mem
        def dummy(x):
            return x

        self.assertTrue(dummy(1), 1)
        self.addCleanup(os.remove, "./LOG.log")

    def test_log_file_exhists(self):
        @mem
        def dummy(x):
            return x

        dummy(1)
        self.assertTrue(os.path.exists("./LOG.log"))
        self.addCleanup(os.remove, "./LOG.log")

    def test_log_file_not_empty(self):
        @mem
        def dummy(x):
            return x

        dummy(1)
        self.assertFalse(os.stat("./LOG.log").st_size == 0)
        self.addCleanup(os.remove, "./LOG.log")

    def test_log_file_content_for_memory_string(self):
        @mem
        def dummy(x):
            return x

        dummy(1)
        self.assertTrue(
            open("./LOG.log", "r").read().find("Size of argument") != -1
        )
        self.addCleanup(os.remove, "./LOG.log")

    def test_log_file_content_for_time_in_BYTES_string(self):
        @mem(unit="bytes")
        def dummy(x):
            return x

        dummy(1)
        self.assertTrue(open("./LOG.log", "r").read().find("bytes") != -1)
        self.addCleanup(os.remove, "./LOG.log")

    def test_log_file_content_for_time_in_MB_string(self):
        @mem(unit="mb")
        def dummy(x):
            return x

        dummy(1)
        self.assertTrue(open("./LOG.log", "r").read().find("MBs") != -1)
        self.addCleanup(os.remove, "./LOG.log")

    def test_log_file_content_for_time_in_GB_string(self):
        @mem(unit="gb")
        def dummy(x):
            return x

        dummy(1)
        self.assertTrue(open("./LOG.log", "r").read().find("GBs") != -1)

    def test_log_file_content_for_time_in_TB_string(self):
        @mem(unit="tb")
        def dummy(x):
            return x

        dummy(1)
        self.assertTrue(open("./LOG.log", "r").read().find("TBs") != -1)

    def test_log_CRITICAL_file(self):
        @mem(level="critical")
        def dummy(x, test=False):
            return x

        dummy(1, test=True)
        self.assertTrue(open("./LOG.log", "r").read().find("CRITICAL") != -1)
        self.addCleanup(os.remove, "./LOG.log")

    def test_log_INFO_file(self):
        @mem(level="info")
        def dummy(x, test=True):
            return x

        dummy(1, test=True)
        self.assertTrue(open("./LOG.log", "r").read().find("INFO") != -1)
        self.addCleanup(os.remove, "./LOG.log")

    def test_log_DEBUG_file(self, test=False):
        @mem(level="debug")
        def dummy(x, test=True):
            return x

        dummy(1, test=True)
        self.assertTrue(open("./LOG.log", "r").read().find("DEBUG") != -1)
        self.addCleanup(os.remove, "./LOG.log")

    def test_log_ERROR_file(self, test=False):
        @mem(level="error")
        def dummy(x, test=True):
            return x

        dummy(1, test=True)
        self.assertTrue(open("./LOG.log", "r").read().find("ERROR") != -1)
        self.addCleanup(os.remove, "./LOG.log")

    def test_log_WARNING_file(self, test=False):
        @mem(level="warning")
        def dummy(x, test=True):
            return x

        dummy(1, test=True)
        self.assertTrue(open("./LOG.log", "r").read().find("WARNING") != -1)
        self.addCleanup(os.remove, "./LOG.log")

    def test_log_name_file_change(self):
        @mem(log_file_name="test")
        def dummy(x):
            return x

        dummy(1)
        self.assertTrue(os.path.exists("./test.log"))
        self.addCleanup(os.remove, "./test.log")

    def test_log_path_file_change(self):
        @mem(log_file_path="test_log_folder")
        def dummy(x):
            return x

        dummy(1)
        self.assertTrue(os.path.exists("./test_log_folder/LOG.log"))
        self.addCleanup(shutil.rmtree, "./test_log_folder")

    def test_raise_run_time_warning(self):

        with self.assertRaises(RuntimeWarning):

            @mem("test_log_folder")
            def dummy(x):
                return x


if __name__ == "__main__":
    unittest.main()
