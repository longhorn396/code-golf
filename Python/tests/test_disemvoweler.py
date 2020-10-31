#!/usr/bin/env python3

"""Test module for disemvoweler.py"""

import unittest
import pycg

class DisemvowelerTestCase(unittest.TestCase):
    """Unit tests for disemvoweler.py"""

    def test_disemvowel(self):
        """disemvowel test"""
        self.assertEqual(pycg.disemvowel("Hello, World!"), "HllWrld eoo")

    def test_sentence(self):
        """More complex test"""
        self.assertEqual(pycg.disemvowel("The quick brown fox jumped over the lazy dog"),
                         "Thqckbrwnfxjmpdvrthlzydg euiooueoeeao")

if __name__ == "__main__": # pragma: no cover
    unittest.main()
