#!/usr/bin/env python3

"""Test module for coin_flip.py"""

import unittest
import pycg

class coin_flipTestCase(unittest.TestCase):
    """Unit tests for coin_flip.py"""

    def _helper(self, result):
        """Logic for testing"""
        segments = result.split("\n")
        self.assertEqual(len(segments[0].split(", ")), 5)
        self.assertEqual(int(segments[1][0]) + int(segments[1][9]), 5)

    def test_reduce(self):
        """Test for the reduce algo"""
        self._helper(pycg.coin_flip_sequence_reduce(5))

    def test_sum(self):
        """Test for the sum algo"""
        self._helper(pycg.coin_flip_sequence_sum(5))

if __name__ == "__main__": # pragma: no cover
    unittest.main()
