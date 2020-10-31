#!/usr/bin/env python3

"""Swedish term that translates to "Robber's Language";
Consonats are doubled with an "o" between them"""

from .common import main_subf as main

def rovarspraket(english):
    """Translates input to rovarspraket"""
    for l, u in zip("bcdfghjklmnpqrstvwxyz", "BCDFGHJKLMNPQRSTVWXYZ"):
        english = f"{u}o{l}".join(f"{l}o{l}".join(english.split(l)).split(u))
    return english

def undo(rovar):
    """Translates rovarspraket into english"""
    for l, u in zip("bcdfghjklmnpqrstvwxyz", "BCDFGHJKLMNPQRSTVWXYZ"):
        rovar = f"{u}".join(f"{l}".join(rovar.split(f"{l}o{l}")).split(f"{u}o{l}"))
    return rovar

if __name__ == "__main__": # pragma: no cover
    main({
        "to_rs": rovarspraket,
        "from_rs": undo
    }, str, lambda x: True, "Input text to translate")
