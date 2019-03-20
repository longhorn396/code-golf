#!/usr/bin/env python3

"""Test module for fibonacci.py"""

import unittest
from fibonacci import dumb_fibonacci, less_dumb_fibonacci, iterative_fibonacci, recursive_fibonacci

class FibonacciTestCase(unittest.TestCase):
    """Unit tests for fibonacci.py"""

    def test_fibonaccis(self):
        """Test for the fibonacci algos"""
        fs = [dumb_fibonacci, less_dumb_fibonacci, iterative_fibonacci, recursive_fibonacci]
        self.assertTrue(all([f(1) == (1, 0, [0]) for f in fs]))
        self.assertTrue(all([f(2) == (2, 1, [0, 1]) for f in fs]))
        self.assertTrue(all([f(5) == (5, 3, [0, 1, 1, 2, 3]) for f in fs]))
        self.assertTrue(all([f(10) == (10, 34, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]) for f in fs]))

if __name__ == "__main__": # pragma: no cover
    unittest.main()
