#!/usr/bin/env python3

"""Typoglycemia is the mind's ability to deciper a mispelled word if the
first and last letters of the word are correct"""

from random import shuffle
from common import main

def typoglycemia(s):
    """Randomizes the internal characters of a string"""
    new_sentence = []
    for word in s.split():
        if len(word) < 4 or "'" in word:
            new_sentence += [word]
        else:
            internal = list(word[1:-1])
            shuffle(internal)
            new_sentence += [word[0] + "".join(internal) + word[-1]]
    return " ".join(new_sentence)

if __name__ == "__main__": # pragma: no cover
    main(typoglycemia, str, "What word(s)?")
