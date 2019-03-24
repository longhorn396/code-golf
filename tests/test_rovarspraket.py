#!/usr/bin/env python3

"""Test module for rovarspraket.py"""

import unittest
from rovarspraket import rovarspraket, undo

class NaturalNumsTestCase(unittest.TestCase):
    """Unit tests for rovarspraket.py"""

    def test_letters(self):
        """Very simple tests"""
        self.assertEqual(rovarspraket("b"), "bob")
        self.assertEqual(rovarspraket("B"), "Bob")

    def test_words(self):
        """Testing with actual words"""
        self.assertEqual(rovarspraket("stubborn"), "sostotubobboborornon")
        self.assertEqual(rovarspraket("Monday"), "Momonondodayoy")

    def test_sentence(self):
        """Testing a sentence"""
        self.assertEqual(rovarspraket("A stubborn Monday."),\
            "A sostotubobboborornon Momonondodayoy.")

    def test_letters_undo(self):
        """Very simple tests"""
        self.assertEqual(undo("bob"), "b")
        self.assertEqual(undo("Bob"), "B")

    def test_words_undo(self):
        """Testing with actual words"""
        self.assertEqual(undo("sostotubobboborornon"), "stubborn")
        self.assertEqual(undo("Momonondodayoy"), "Monday")

    def test_sentence_undo(self):
        """Testing a sentence"""
        self.assertEqual(undo("A sostotubobboborornon Momonondodayoy."), "A stubborn Monday.")

if __name__ == "__main__": # pragma: no cover
    unittest.main()
