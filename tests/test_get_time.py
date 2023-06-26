# some_name_test.py
import unittest
from unittest.mock import MagicMock
import os
import sys
import shutil
import numpy as np

sys.path.append("../")

from PyDecLog import _get_time


class TestlPrint(unittest.TestCase):
    def test_get_time_SEC(self):

        elapsed_time = _get_time(1, 3, "sec")
        self.assertEqual(elapsed_time, 2)

    def test_get_time_MIN(self):

        elapsed_time = _get_time(1, 3, "min")

        np.testing.assert_array_almost_equal(elapsed_time, 2 / 60, decimal=3)

    def test_get_time_HR(self):

        elapsed_time = _get_time(1, 3, "hr")

        np.testing.assert_array_almost_equal(elapsed_time, 2 / 3660, decimal=3)

    def test_raise_type_error(self):

        with self.assertRaises(TypeError):
            _get_time(1, 3, "year")


if __name__ == "__main__":
    unittest.main()
