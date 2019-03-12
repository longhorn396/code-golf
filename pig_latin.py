#!/usr/bin/env python3

"""Module to translate english into Pig Latin"""

from string import punctuation
from common import main_subf as main

def simple_translate(english):
    """Simplest translation"""
    words = english.lower().translate(str.maketrans("", "", punctuation)).split()
    return " ".join([word[1:] + word[0] + "ay" for word in words])

if __name__ == "__main__":
    main({
        "simple": simple_translate
    }, str, lambda x: not any(char.isdigit() for char in x),\
    "Type text to translate (no numbers)")
