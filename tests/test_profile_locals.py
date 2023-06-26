# some_name_test.py
import unittest
from unittest.mock import MagicMock
import os
import sys
import shutil

sys.path.append("../")

from PyDecLog import profile_locals as profile


class TestProfileLocals(unittest.TestCase):
    def test_same_function_return(self):
        @profile
        def dummy(x, test=True):
            "Do nothing"
            return x

        dummy.locals
        self.assertTrue(dummy(1, test=False), 1)

    def test_has_locals_attributes(self):
        @profile
        def dummy(x):
            "Do nothing"
            return x

        dummy(1)
        self.assertTrue(hasattr(dummy, "locals"))

    def test_locals_attributes_values(self):
        @profile
        def dummy(x):
            "Do nothing"
            return x

        dummy(1)
        self.assertTrue(dummy.locals["x"], 1)


if __name__ == "__main__":
    unittest.main()
