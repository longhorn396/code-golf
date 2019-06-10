#!/usr/bin/env python3

"""Disemvowel strings"""

from string import ascii_letters
from common import main

def disemvowel(s):
    """Separate the vowels and consonants of a string"""
    cons, vows = "", ""
    for c in s:
        if c in "aeiouAEIOU":
            vows += c
        elif c in ascii_letters:
            cons += c
    return f"{cons} {vows}"

if __name__ == "__main__": # pragma: no cover
    main(disemvowel, str, "What word(s)?")
