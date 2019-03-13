#!/usr/bin/env python3

"""Test module for pig_latin.py"""

import unittest
from string import punctuation
import pig_latin

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

    def help_test(self, fun, english, translated):
        """Helper for most tests"""
        for i, en in enumerate(english):
            assert fun(en).lower() == translated[i].lower()

    def test_simple_con(self):
        """Basic functionality of simple function"""
        self.help_test(pig_latin.simple_translate, self.con_en, self.con_pl)

    def test_simple_punct(self):
        """Functionality of punctuation in the simple function"""
        assert pig_latin.simple_translate(punctuation) == ""

    def test_full_con(self):
        """Basic functionality of full function"""
        self.help_test(pig_latin.full_translation, self.con_en, self.con_pl)

    def test_full_ccl(self):
        """Beginning consonant cluster functionality of full function"""
        self.help_test(pig_latin.full_translation, self.ccl_en, self.ccl_pl)

    def test_full_vow(self):
        """Beginning vowel functionality of full function"""
        self.help_test(pig_latin.full_translation, self.vow_en, self.vow_pl)

    def test_full_punct(self):
        """Functionality of punctuation in the full function"""
        assert pig_latin.full_translation(punctuation) == punctuation

    def test_full_para(self):
        """Paragraph functionality of full function"""
        assert pig_latin.full_translation(self.para_en) == self.para_pl

if __name__ == "__main__":  # pragma: no cover
    unittest.main()
