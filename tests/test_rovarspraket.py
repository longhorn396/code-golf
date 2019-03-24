#!/usr/bin/env python3

"""Test module for rovarspraket.py"""

import unittest
from rovarspraket import rovarspraket

class NaturalNumsTestCase(unittest.TestCase):
    """Unit tests for rovarspraket.py"""

    def test_letters(self):
        """Very simple tests"""
        self.assertEqual(rovarspraket("b"), "bob")
        self.assertEqual(rovarspraket("B"), "Bob")
        self.assertEqual(rovarspraket("m"), "mom")
        self.assertEqual(rovarspraket("M"), "Mom")

    def test_words(self):
        """Testing with actual words"""
        self.assertEqual(rovarspraket("stubborn"), "sostotubobboborornon")
        self.assertEqual(rovarspraket("Monday"), "Momonondodayoy")

    def test_sentence(self):
        """Testing a sentence"""
        self.assertEqual(rovarspraket("A stubborn Monday."),\
            "A sostotubobboborornon Momonondodayoy.")
