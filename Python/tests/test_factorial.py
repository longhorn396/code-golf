#!/usr/bin/env python3

"""Test module for factorial.py"""

import unittest
import pycg

class FactorialTestCase(unittest.TestCase):
    """Unit tests for factorial.py"""

    def test_factorials(self):
        """Test for the factorial algos"""
        funs = [pycg.for_factorial, pycg.range_factorial, pycg.recursive_factorial,\
            pycg.reduce1_factorial, pycg.reduce2_factorial, pycg.tail_factorial,\
            pycg.while_factorial]
        self.assertTrue(all([fun(5) == 120 for fun in funs]))

if __name__ == "__main__": # pragma: no cover
    unittest.main()
