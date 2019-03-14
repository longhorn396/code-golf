#!/usr/bin/env python3

"""Test module for factorial.py"""

import unittest
from factorial import for_factorial, range_factorial, recursive_factorial, reduce1_factorial,\
            reduce2_factorial, tail_factorial, while_factorial

class FactorialTestCase(unittest.TestCase):
    """Unit tests for factorial.py"""

    def test_factorials(self):
        """Test for the factorial algos"""
        funs = [for_factorial, range_factorial, recursive_factorial, reduce1_factorial,\
            reduce2_factorial, tail_factorial, while_factorial]
        results = [fun(5) == 120 for fun in funs]
        assert all(results)

if __name__ == "__main__": # pragma: no cover
    unittest.main()
