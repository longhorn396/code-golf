#!/usr/bin/env python3

"""Generates a sequence of coin flips"""

from random import choice
from functools import reduce
from operator import add

def coin_flip_sequence(tries):
    """Prints the results of coin flips and the totals of the results"""
    assert tries >= 1
    results = [choice([0, 1]) for _ in range(0, tries)]
    tails = reduce(add, results, 0)
    heads = len(results) - tails
    result = ", ".join([["Heads", "Tails"][flip] for flip in results])
    return result + "\n{:d} Heads; {:d} Tails".format(heads, tails)

if __name__ == "__main__":
    try:
        print(coin_flip_sequence(int(input("How many coins do you want to flip?\n"))))
    except AssertionError:
        print("You gave an invalid argument")
