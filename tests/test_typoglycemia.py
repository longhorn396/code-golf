#!/usr/bin/env python3

"""Test module for typoglycemia.py"""

import unittest
from typoglycemia import typoglycemia

class TypoglycemiaTestCase(unittest.TestCase):
    """Unit tests for typoglycemia.py"""

    def test_null_case(self):
        """Shouldn't do anything"""
        self.assertEqual(typoglycemia("I can't do it"), "I can't do it")

    def test_typoglycemia(self):
        """typoglycemia test"""
        typo = typoglycemia("I deciphered a mispelled word")
        self.assertEqual(len(typo), 29)
        self.assertEqual(len(typo.split(" ")), 5)
        self.assertTrue(typo.startswith("I d"))
        self.assertTrue(typo.endswith("d"))

if __name__ == "__main__": # pragma: no cover
    unittest.main()
