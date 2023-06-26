from pyDecLog import _get_mem
import unittest
from unittest.mock import MagicMock
import os
import sys
import shutil
import numpy as np
from pympler.asizeof import asizeof


class TestlGetMemorySize(unittest.TestCase):
    def test_get_mem_BYTES(self):

        a = ["a"] * 1000
        memory_used, memory_unit = _get_mem("bytes", a)
        self.assertEqual(memory_used, asizeof(a))
        self.assertEqual(memory_unit, "bytes")

    def test_get_mem_MB(self):

        a = ["a"] * 1000
        memory_used, memory_unit = _get_mem("mb", a)
        self.assertEqual(memory_used, asizeof(a) / 1.0e6)
        self.assertEqual(memory_unit, "MBs")

    def test_get_mem_GB(self):

        a = ["a"] * 1000
        memory_used, memory_unit = _get_mem("gb", a)
        self.assertEqual(memory_used, asizeof(a) / 1.0e9)
        self.assertEqual(memory_unit, "GBs")

    def test_get_mem_TB(self):

        a = ["a"] * 1000
        memory_used, memory_unit = _get_mem("tb", a)
        self.assertEqual(memory_used, asizeof(a) / 1.0e12)
        self.assertEqual(memory_unit, "TBs")

    def test_raise_type_error(self):

        with self.assertRaises(TypeError):
            a = ["a"] * 1000
            _get_mem("pb", a)


if __name__ == "__main__":
    unittest.main()
