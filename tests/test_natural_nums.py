#!/usr/bin/env python3

"""Test module for natural_nums.py"""

import unittest
from natural_nums import find_nth_natural_number

class NaturalNumsTestCase(unittest.TestCase):
    """Unit tests for natural_nums.py"""

    out_format = "The natural number is {} in {}"

    def test_one(self):
        """Basic test"""
        self.assertEqual(find_nth_natural_number(1, 1), self.out_format.format(1, 1))

    def test_given(self):
        """Test given in problem statement"""
        self.assertEqual(find_nth_natural_number(17, 20), self.out_format.format(3, 13))

    def test_task(self):
        """Test for problem in problem statement"""
        self.assertEqual(find_nth_natural_number(1986, 1000), self.out_format.format(8, 698))

    def test_too_small(self):
        """Assert fails when range is too small"""
        self.assertRaises(AssertionError, find_nth_natural_number, 1986, 20)

if __name__ == "__main__":  # pragma: no cover
    unittest.main()
