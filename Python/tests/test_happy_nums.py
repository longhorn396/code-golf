#!/usr/bin/env python3

"""Test module for happy_nums.py"""

import unittest
import pycg

class HappyNumsTestCase(unittest.TestCase):
    """Unit tests for happy_nums.py"""

    def test_happiness(self):
        """is_happy test"""
        nums = [7, 13, 69, 420]
        results = [True, True, False, False]
        self.assertListEqual([pycg.is_happy(num) for num in nums], results)

    def test_searching(self):
        """search test"""
        results = [1, 7, 10, 13, 19, 23, 28, 31, 32, 44, 49, 68]
        self.assertListEqual(pycg.search(12), results)

if __name__ == "__main__": # pragma: no cover
    unittest.main()
