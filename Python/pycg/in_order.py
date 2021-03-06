#!/usr/bin/env python3

"""Evaluate strings for alphabetical order"""

from string import ascii_lowercase
from .common import main

def in_order(words):
    """Wrapper for each word in `words`"""
    res = [f"{word} -{'' if w_in_order(word) else ' not'} in order" for word in words.split(" ")]
    return " ".join(res)

def w_in_order(word):
    """Evaluate if the characters in `word` are in alphabetical order"""
    for i, character in enumerate(word.lower()[:len(word) - 1]):
        if character in ascii_lowercase and character <= word[i + 1]:
            continue
        return False
    return True

if __name__ == "__main__": # pragma: no cover
    main(in_order, str, "What word(s)?")
