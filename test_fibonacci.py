#!/usr/bin/env python3

"""Test module for fibonacci.py"""

import unittest
from fibonacci import dumb_fibonacci, less_dumb_fibonacci, iterative_fibonacci, recursive_fibonacci

class FibonacciTestCase(unittest.TestCase):
    """Unit tests for fibonacci.py"""

    def test_fibonaccis(self):
        """Test for the fibonacci algos"""
        funs = [dumb_fibonacci, less_dumb_fibonacci, iterative_fibonacci, recursive_fibonacci]
        assert all([fun(1) == (1, 0, [0]) for fun in funs])
        assert all([fun(2) == (2, 1, [0, 1]) for fun in funs])
        assert all([fun(5) == (5, 3, [0, 1, 1, 2, 3]) for fun in funs])
        assert all([fun(10) == (10, 34, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]) for fun in funs])

if __name__ == "__main__": # pragma: no cover
    unittest.main()
