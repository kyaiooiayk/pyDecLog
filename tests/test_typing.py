from pyDecLog import typing as typ
import unittest
import os
import shutil


class TestTipying(unittest.TestCase):
    def test_same_function_return(self):
        @typ
        def dummy(x):
            "Do nothing"
            return x

        self.assertTrue(dummy(1), 1)
        self.addCleanup(os.remove, "./LOG.log")

    def test_log_file_exhists(self):
        @typ
        def dummy(x):
            "Do nothing"
            return x

        dummy(1)
        self.assertTrue(os.path.exists("./LOG.log"))
        self.addCleanup(os.remove, "./LOG.log")

    def test_log_file_not_empty(self):
        @typ
        def dummy(x):
            "Do nothing"
            return x

        dummy(1)
        self.assertFalse(os.stat("./LOG.log").st_size == 0)
        self.addCleanup(os.remove, "./LOG.log")

    def test_log_file_content_for_type_string(self):
        @typ
        def dummy(x):
            "Do nothing"
            return x

        dummy(1)
        self.assertTrue(
            open("./LOG.log", "r").read().find("DEBUG Argument's type:") != -1
        )
        self.addCleanup(os.remove, "./LOG.log")

    def test_log_CRITICAL_file(self):
        @typ(level="critical")
        def dummy(x, test=False):
            "Do nothing"
            return x

        dummy(1, test=True)
        self.assertTrue(
            open("./LOG.log", "r").read().find("CRITICAL Argument's type:")
            != -1
        )
        self.addCleanup(os.remove, "./LOG.log")

    def test_log_INFO_file(self):
        @typ(level="info")
        def dummy(x, test=False):
            "Do nothing"
            return x

        dummy(1, test=True)
        self.assertTrue(
            open("./LOG.log", "r").read().find("INFO Argument's type:") != -1
        )
        self.addCleanup(os.remove, "./LOG.log")

    def test_log_DEBUG_file(self):
        @typ(level="debug")
        def dummy(x, test=False):
            "Do nothing"
            return x

        dummy(1, test=True)
        self.assertTrue(
            open("./LOG.log", "r").read().find("DEBUG Argument's type:") != -1
        )
        self.addCleanup(os.remove, "./LOG.log")

    def test_log_ERROR_file(self):
        @typ(level="error")
        def dummy(x, test=False):
            "Do nothing"
            return x

        dummy(1, test=True)
        self.assertTrue(
            open("./LOG.log", "r").read().find("ERROR Argument's type:") != -1
        )
        self.addCleanup(os.remove, "./LOG.log")

    def test_log_WARNING_file(self):
        @typ(level="warning")
        def dummy(x, test=False):
            "Do nothing"
            return x

        dummy(1, test=True)
        self.assertTrue(
            open("./LOG.log", "r").read().find("WARNING Argument's type:")
            != -1
        )
        self.addCleanup(os.remove, "./LOG.log")

    def test_log_name_file_change(self):
        @typ(log_file_name="test")
        def dummy(x):
            "Do nothing"
            return x

        dummy(1)
        self.assertTrue(os.path.exists("./test.log"))
        self.addCleanup(os.remove, "./test.log")

    def test_log_path_file_change(self):
        @typ(log_file_path="test_log_folder")
        def dummy(x):
            "Do nothing"
            return x

        dummy(1)
        self.assertTrue(os.path.exists("./test_log_folder/LOG.log"))
        self.addCleanup(shutil.rmtree, "./test_log_folder")

    def test_raise_run_time_warning(self):

        with self.assertRaises(RuntimeWarning):

            @typ("test_log_folder")
            def dummy(x):
                return x


if __name__ == "__main__":
    unittest.main()
