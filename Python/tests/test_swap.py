#!/usr/bin/env python3

"""Test module for swap.py"""

import unittest
import pycg

class swapTestCase(unittest.TestCase):
    """Unit tests for swap.py"""

    def test_swaps(self):
        """Test for the swap algos"""
        x, y = 5641, 74351
        funs = [pycg.temp_swap, pycg.temp2_swap, pycg.tuple_swap, pycg.return_swap, pycg.xor_swap]
        self.assertTrue(all([fun(x, y) == (y, x) for fun in funs]))

if __name__ == "__main__": # pragma: no cover
    unittest.main()
