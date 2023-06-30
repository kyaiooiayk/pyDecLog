from pyDecLog import description as desc
import unittest
import os
import shutil


class TestDescription(unittest.TestCase):
    def test_same_function_return(self):
        @desc
        def dummy(x):
            "Do nothing"
            return x

        self.assertTrue(dummy(1), 1)
        self.addCleanup(os.remove, "./LOG.log")

    def test_log_file_exhists(self):
        @desc
        def dummy(x):
            "Do nothing"
            return x

        dummy(1)
        self.assertTrue(os.path.exists("./LOG.log"))
        self.addCleanup(os.remove, "./LOG.log")

    def test_log_file_not_empty(self):
        @desc
        def dummy(x):
            "Do nothing"
            return x

        dummy(1)
        self.assertFalse(os.stat("./LOG.log").st_size == 0)
        self.addCleanup(os.remove, "./LOG.log")

    def test_log_file_content_for_description_string(self):
        @desc
        def dummy(x):
            "Do nothing"
            return x

        dummy(1)
        self.assertTrue(
            open("./LOG.log", "r").read().find("DEBUG Method's description:")
            != -1
        )
        self.addCleanup(os.remove, "./LOG.log")

    def test_log_CRITICAL_file(self):
        @desc(level="critical")
        def dummy(x):
            "Do nothing"
            return x

        dummy(1)
        self.assertTrue(
            open("./LOG.log", "r")
            .read()
            .find("CRITICAL Method's description:")
            != -1
        )
        self.addCleanup(os.remove, "./LOG.log")

    def test_log_INFO_file(self):
        @desc(level="info")
        def dummy(x):
            "Do nothing"
            return x

        dummy(1)
        self.assertTrue(
            open("./LOG.log", "r").read().find("INFO Method's description:")
            != -1
        )
        self.addCleanup(os.remove, "./LOG.log")

    def test_log_DEBUG_file(self):
        @desc(level="debug")
        def dummy(x):
            "Do nothing"
            return x

        dummy(1)
        self.assertTrue(
            open("./LOG.log", "r").read().find("DEBUG Method's description:")
            != -1
        )
        self.addCleanup(os.remove, "./LOG.log")

    def test_log_ERROR_file(self):
        @desc(level="error")
        def dummy(x):
            "Do nothing"
            return x

        dummy(1)
        self.assertTrue(
            open("./LOG.log", "r").read().find("ERROR Method's description:")
            != -1
        )
        self.addCleanup(os.remove, "./LOG.log")

    def test_log_WARNING_file(self):
        @desc(level="warning")
        def dummy(x):
            "Do nothing"
            return x

        dummy(1)
        self.assertTrue(
            open("./LOG.log", "r").read().find("WARNING Method's description:")
            != -1
        )
        self.addCleanup(os.remove, "./LOG.log")

    def test_log_name_file_change(self):
        @desc(log_file_name="test")
        def dummy(x):
            "Do nothing"
            return x

        dummy(1)
        self.assertTrue(os.path.exists("./test.log"))
        self.addCleanup(os.remove, "./test.log")

    def test_log_path_file_change(self):
        @desc(log_file_path="test_log_folder")
        def dummy(x):
            "Do nothing"
            return x

        dummy(1)
        self.assertTrue(os.path.exists("./test_log_folder/LOG.log"))
        self.addCleanup(shutil.rmtree, "./test_log_folder")

    def test_raise_run_time_warning(self):

        with self.assertRaises(RuntimeWarning):

            @desc("test_log_folder")
            def dummy(x):
                return x


if __name__ == "__main__":
    unittest.main()
