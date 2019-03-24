#!/usr/bin/env python3

"""Sweedish term that translates to "Robber's Language";
Consonats are doubled with an "o" between them"""

from common import main

def rovarspraket(english):
    """Translates input to rovarspraket"""
    for l, u in zip("bcdfghjklmnpqrstvwxyz", "BCDFGHJKLMNPQRSTVWXYZ"):
        english = f"{u}o{l}".join(f"{l}o{l}".join(english.split(l)).split(u))
    return english

if __name__ == "__main__": # pragma: no cover
    main(rovarspraket, str, "Input text to translate")
