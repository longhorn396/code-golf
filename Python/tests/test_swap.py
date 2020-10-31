#!/usr/bin/env python3

"""Test module for swap.py"""

import unittest
import pycg

class SwapTestCase(unittest.TestCase):
    """Unit tests for swap.py"""

    def test_swaps(self):
        """Test for the swap algos"""
        i, j = 5641, 74351
        subfs = [pycg.temp_swap, pycg.temp2_swap, pycg.tuple_swap, pycg.return_swap, pycg.xor_swap]
        self.assertTrue(all([fun(i, j) == (j, i) for fun in subfs]))

if __name__ == "__main__": # pragma: no cover
    unittest.main()
