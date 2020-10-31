#!/usr/bin/env python3

"""Swedish term that translates to "Robber's Language";
Consonats are doubled with an "o" between them"""

from .common import main_subf as main

def rovarspraket(english):
    """Translates input to rovarspraket"""
    for low, upper in zip("bcdfghjklmnpqrstvwxyz", "BCDFGHJKLMNPQRSTVWXYZ"):
        english = f"{upper}o{low}".join(f"{low}o{low}".join(english.split(low)).split(upper))
    return english

def undo(rovar):
    """Translates rovarspraket into english"""
    for low, upper in zip("bcdfghjklmnpqrstvwxyz", "BCDFGHJKLMNPQRSTVWXYZ"):
        rovar = f"{upper}".join(f"{low}".join(rovar.split(f"{low}o{low}")).split(f"{upper}o{low}"))
    return rovar

if __name__ == "__main__": # pragma: no cover
    main({
        "to_rs": rovarspraket,
        "from_rs": undo
    }, str, lambda x: True, "Input text to translate")
