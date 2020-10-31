#!/usr/bin/env python3

"""Test module for pig_latin.py
Examples obtained from https://en.wikipedia.org/wiki/Pig_Latin#Rules"""

import unittest
from string import punctuation
import pycg

class PigLatinTestCase(unittest.TestCase):
    """Unit tests for pig_latin.py"""

    con_en = ["pig", "latin", "banana", "happy", "duck", "me", "too"]
    con_pl = ["igpay", "atinlay", "ananabay", "appyhay", "uckday", "emay", "ootay"]

    ccl_en = ["smile", "string", "stupid", "glove", "trash", "floor", "store"]
    ccl_pl = ["ilesmay", "ingstray", "upidstay", "oveglay", "ashtray", "oorflay", "orestay"]

    vow_en = ["eat", "omelet", "are", "egg", "explain", "always", "ends", "I"]
    vow_pl = ["eatway", "omeletway", "areway", "eggway", "explainway", "alwaysway", "endsway",\
        "Iway"]

    para_en = "Pig, eat. Smile? It's easy!"
    para_pl = "Igpay, eatway. Ilesmay? It'sway easyway!"

    def help_test(self, fun, raw, translated):
        """Helper for most tests"""
        for i, text in enumerate(raw):
            self.assertEqual(fun(text).lower(), translated[i].lower())

    def test_simple_con(self):
        """Basic functionality of simple function"""
        self.help_test(pycg.simple_translate, self.con_en, self.con_pl)

    def test_simple_punct(self):
        """Functionality of punctuation in the simple function"""
        self.assertEqual(pycg.simple_translate(punctuation), "")

    def test_undo_con(self):
        """Basic functionality of simple_undo function"""
        self.help_test(pycg.simple_undo, self.con_pl, self.con_en)

    def test_full_con(self):
        """Basic functionality of full function"""
        self.help_test(pycg.full_translation, self.con_en, self.con_pl)

    def test_full_ccl(self):
        """Beginning consonant cluster functionality of full function"""
        self.help_test(pycg.full_translation, self.ccl_en, self.ccl_pl)

    def test_full_vow(self):
        """Beginning vowel functionality of full function"""
        self.help_test(pycg.full_translation, self.vow_en, self.vow_pl)

    def test_full_punct(self):
        """Functionality of punctuation in the full function"""
        self.assertEqual(pycg.full_translation(punctuation), punctuation)

    def test_full_para(self):
        """Paragraph functionality of full function"""
        self.assertEqual(pycg.full_translation(self.para_en), self.para_pl)

    def test_full_undo(self):
        """Basic functionality of full_undo"""
        self.help_test(pycg.full_undo, self.con_pl, self.con_en)

    def test_full_undo_ccl(self):
        """Consonant clusters passed to full_undo will not translate correctly"""
        for word in self.ccl_en:
            self.assertNotEqual(word, pycg.full_undo(pycg.full_translation(word)))

    def test_full_undo_vow(self):
        """Vowel functionality of full_undo"""
        self.help_test(pycg.full_undo, self.vow_pl, self.vow_en)

if __name__ == "__main__":  # pragma: no cover
    unittest.main()
