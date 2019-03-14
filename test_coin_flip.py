#!/usr/bin/env python3

"""Test module for coin_flip.py"""

import unittest
from coin_flip import coin_flip_sequence_reduce, coin_flip_sequence_sum

class coin_flipTestCase(unittest.TestCase):
    """Unit tests for coin_flip.py"""

    def test_reduce(self):
        """Test for the reduce algo"""
        result = coin_flip_sequence_reduce(5)
        segments = result.split("\n")
        # TODO: analyze segments[0]
        num_heads = int(segments[1][0])
        num_tails = int(segments[1][9])
        assert num_heads + num_tails == 5

    def test_sum(self):
        """Test for the sum algo"""
        result = coin_flip_sequence_sum(5)
        segments = result.split("\n")
        # TODO: analyze segments[0]
        num_heads = int(segments[1][0])
        num_tails = int(segments[1][9])
        assert num_heads + num_tails == 5

if __name__ == "__main__": # pragma: no cover
    unittest.main()
