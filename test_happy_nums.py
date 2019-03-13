#!/usr/bin/env python3

"""Test module for happy_nums.py"""

import unittest
from happy_nums import search, is_happy

class HappyNumsTestCase(unittest.TestCase):
    """Unit tests for happy_nums.py"""

    out_format = "The happy number is {} in {}"

    def test_happyiness(self):
        """is_happy test"""
        nums = [7, 13, 69, 420]
        results = [True, True, False, False]
        assert [is_happy(num) for num in nums] == results

    def test_searching(self):
        """search test"""
        results = [1, 7, 10, 13, 19, 23, 28, 31, 32, 44, 49, 68]
        assert search(12) == results

if __name__ == "__main__": # pragma: no cover
    unittest.main()
