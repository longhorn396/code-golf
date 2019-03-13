#!/usr/bin/env python3

"""Test module for coin_flip.py"""

import unittest
from coin_flip import coin_flip_sequence_reduce, coin_flip_sequence_sum

class coin_flipTestCase(unittest.TestCase):
    """Unit tests for coin_flip.py"""

    def test_happyiness(self):
        """Test for the coin_flip algos"""
        funs = []
        results = [120 == fun(5) for fun in funs]
        assert all(results)

if __name__ == "__main__": # pragma: no cover
    unittest.main()
