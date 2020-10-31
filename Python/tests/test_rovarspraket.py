#!/usr/bin/env python3

"""Test module for rovarspraket.py"""

import unittest
import pycg

class NaturalNumsTestCase(unittest.TestCase):
    """Unit tests for rovarspraket.py"""

    def test_letters(self):
        """Very simple tests"""
        self.assertEqual(pycg.rovarspraket("b"), "bob")
        self.assertEqual(pycg.rovarspraket("B"), "Bob")

    def test_words(self):
        """Testing with actual words"""
        self.assertEqual(pycg.rovarspraket("stubborn"), "sostotubobboborornon")
        self.assertEqual(pycg.rovarspraket("Monday"), "Momonondodayoy")

    def test_sentence(self):
        """Testing a sentence"""
        self.assertEqual(pycg.rovarspraket("A stubborn Monday."),\
            "A sostotubobboborornon Momonondodayoy.")

    def test_letters_undo(self):
        """Very simple tests"""
        self.assertEqual(pycg.undo("bob"), "b")
        self.assertEqual(pycg.undo("Bob"), "B")

    def test_words_undo(self):
        """Testing with actual words"""
        self.assertEqual(pycg.undo("sostotubobboborornon"), "stubborn")
        self.assertEqual(pycg.undo("Momonondodayoy"), "Monday")

    def test_sentence_undo(self):
        """Testing a sentence"""
        self.assertEqual(pycg.undo("A sostotubobboborornon Momonondodayoy."), "A stubborn Monday.")

if __name__ == "__main__": # pragma: no cover
    unittest.main()
