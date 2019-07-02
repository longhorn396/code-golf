#!/usr/bin/env python3

"""Test module for swap.py"""

import unittest
from swap import temp_swap, temp2_swap, tuple_swap, return_swap, xor_swap

class swapTestCase(unittest.TestCase):
    """Unit tests for swap.py"""

    def test_swaps(self):
        """Test for the swap algos"""
        x, y = 5641, 74351
        funs = [temp_swap, temp2_swap, tuple_swap, return_swap, xor_swap]
        self.assertTrue(all([fun(x, y) == (y, x) for fun in funs]))

if __name__ == "__main__": # pragma: no cover
    unittest.main()
