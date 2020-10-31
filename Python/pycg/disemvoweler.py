#!/usr/bin/env python3

"""Disemvowel strings"""

from string import ascii_letters
from .common import main

def disemvowel(text):
    """Separate the vowels and consonants of a string"""
    cons, vows = "", ""
    for character in text:
        if character in "aeiouAEIOU":
            vows += character
        elif character in ascii_letters:
            cons += character
    return f"{cons} {vows}"

if __name__ == "__main__": # pragma: no cover
    main(disemvowel, str, "What word(s)?")
