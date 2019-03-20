#!/usr/bin/env python3

"""Module to translate english into Pig Latin
Rules obtained from https://en.wikipedia.org/wiki/Pig_Latin#Rules"""

from string import punctuation
from common import main_subf as main

def simple_translate(english):
    """Simplest translation"""
    words = english.lower().translate(str.maketrans("", "", punctuation)).split()
    return " ".join([word[1:] + word[0] + "ay" for word in words])

def simple_undo(pl):
    """Undoing simplest translation"""
    pl += " "
    words = pl.split("ay ")
    return " ".join([word[-1] + word[:-1] for word in words[:-1]])

def full_translation(english):
    """More advanced and correct translation"""
    # TODO: go from full pl back to english
    words = english.lower().split()
    vowels = "AaEeIiOoUu"
    ending_punct = ".?!"
    pig_latin = []
    cap_next = True
    for word in words:
        if word[0] in vowels:
            if word[-1] in punctuation:
                plw = word[:len(word) - 1] + "way" + word[-1]
            else:
                plw = word + "way"
        else:
            plw = ""
            for char in word:
                if char not in vowels:
                    plw += char
                else:
                    if word[-1] in punctuation:
                        plw = word[word.index(char):len(word) - 1] + plw + "ay" + word[-1]
                    else:
                        plw = word[word.index(char):] + plw + "ay"
                    break
        if cap_next:
            plw = plw[0].upper() + plw[1:]
            cap_next = False
        cap_next = plw[-1] in ending_punct
        pig_latin += [plw]
    return " ".join(pig_latin)

if __name__ == "__main__": # pragma: no cover
    main({
        "simple": simple_translate,
        "sim_undo": simple_undo,
        "complex": full_translation
    }, str, lambda x: not any(char.isdigit() for char in x),\
    "Type text to translate (no numbers)")
