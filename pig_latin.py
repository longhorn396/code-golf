#!/usr/bin/env python3

"""Module to translate english into Pig Latin"""

from string import punctuation
from common import main_subf as main

def simple_translate(english):
    """Simplest translation"""
    words = english.lower().translate(str.maketrans("", "", punctuation)).split()
    return " ".join([word[1:] + word[0] + "ay" for word in words])

def full_translation(english):
    """More advanced and correct translation"""
    vowels = "AaEeIiOoUu"
    words = english.lower().split()
    pig_latin = []
    for word in words:
        beginning = word[0]
        if beginning in vowels:
            if word[-1] in punctuation:
                pig_latin += [word[:len(word) - 1] + "way" + word[-1]]
            else:
                pig_latin += [word + "way"]
        else:
            cluster = ""
            for char in word:
                if char not in vowels:
                    cluster += char
                else:
                    if word[-1] in punctuation:
                        pig_latin += \
                            [word[word.index(char):len(word) - 1] + cluster + "ay" + word[-1]]
                    else:
                        pig_latin += [word[word.index(char):] + cluster + "ay"]
                    break
    return " ".join(pig_latin)

if __name__ == "__main__":
    main({
        "simple": simple_translate,
        "complex": full_translation
    }, str, lambda x: not any(char.isdigit() for char in x),\
    "Type text to translate (no numbers)")
