from pyDecLog import timing as tim
import unittest
import os
import shutil


class TestTiming(unittest.TestCase):
    def test_same_function_return(self):
        @tim
        def dummy(x):
            return x

        self.assertTrue(dummy(1), 1)
        self.addCleanup(os.remove, "./LOG.log")

    def test_log_file_exhists(self):
        @tim
        def dummy(x):
            return x

        dummy(1)
        self.assertTrue(os.path.exists("./LOG.log"))
        self.addCleanup(os.remove, "./LOG.log")

    def test_log_file_not_empty(self):
        @tim
        def dummy(x):
            return x

        dummy(1)
        self.assertFalse(os.stat("./LOG.log").st_size == 0)
        self.addCleanup(os.remove, "./LOG.log")

    def test_log_file_content_for_time_string(self):
        @tim
        def dummy(x):
            return x

        dummy(1)
        self.assertTrue(
            open("./LOG.log", "r").read().find("was executed in") != -1
        )
        self.addCleanup(os.remove, "./LOG.log")

    def test_log_file_content_for_time_in_SEC_string(self):
        @tim(unit="sec")
        def dummy(x):
            return x

        dummy(1)
        self.assertTrue(open("./LOG.log", "r").read().find("sec") != -1)
        self.addCleanup(os.remove, "./LOG.log")

    def test_log_file_content_for_time_in_MIN_string(self):
        @tim(unit="min")
        def dummy(x):
            return x

        dummy(1)
        self.assertTrue(open("./LOG.log", "r").read().find("min") != -1)
        self.addCleanup(os.remove, "./LOG.log")

    def test_log_file_content_for_time_in_HR_string(self):
        @tim(unit="hr")
        def dummy(x):
            return x

        dummy(1)
        self.assertTrue(open("./LOG.log", "r").read().find("hr") != -1)

    def test_log_CRITICAL_file(self):
        @tim(level="critical")
        def dummy(x):
            return x

        dummy(1)
        self.assertTrue(open("./LOG.log", "r").read().find("CRITICAL") != -1)
        self.addCleanup(os.remove, "./LOG.log")

    def test_log_INFO_file(self):
        @tim(level="info")
        def dummy(x):
            return x

        dummy(1)
        self.assertTrue(open("./LOG.log", "r").read().find("INFO") != -1)
        self.addCleanup(os.remove, "./LOG.log")

    def test_log_DEBUG_file(self):
        @tim(level="debug")
        def dummy(x):
            return x

        dummy(1)
        self.assertTrue(open("./LOG.log", "r").read().find("DEBUG") != -1)
        self.addCleanup(os.remove, "./LOG.log")

    def test_log_ERROR_file(self):
        @tim(level="error")
        def dummy(x):
            return x

        dummy(1)
        self.assertTrue(open("./LOG.log", "r").read().find("ERROR") != -1)
        self.addCleanup(os.remove, "./LOG.log")

    def test_log_WARNING_file(self):
        @tim(level="warning")
        def dummy(x):
            return x

        dummy(1)
        self.assertTrue(open("./LOG.log", "r").read().find("WARNING") != -1)
        self.addCleanup(os.remove, "./LOG.log")

    def test_log_name_file_change(self):
        @tim(log_file_name="test")
        def dummy(x):
            return x

        dummy(1)
        self.assertTrue(os.path.exists("./test.log"))
        self.addCleanup(os.remove, "./test.log")

    def test_log_path_file_change(self):
        @tim(log_file_path="test_log_folder")
        def dummy(x):
            return x

        dummy(1)
        self.assertTrue(os.path.exists("./test_log_folder/LOG.log"))
        self.addCleanup(shutil.rmtree, "./test_log_folder")

    def test_raise_run_time_warning(self):

        with self.assertRaises(RuntimeWarning):

            @tim("test_log_folder")
            def dummy(x):
                return x


if __name__ == "__main__":
    unittest.main()
