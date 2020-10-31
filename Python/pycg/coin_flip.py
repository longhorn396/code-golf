#!/usr/bin/env python3

"""Generates a sequence of coin flips"""

from random import choice
from functools import reduce
from operator import add
from .common import main_subf as main
from .common import compare_subfs as compare

def output_results(results, way):
    """Helper method with most of the logic"""
    tails = way(results)
    heads = len(results) - tails
    result = ", ".join([["Heads", "Tails"][flip] for flip in results])
    return result + f"\n{heads} Heads; {tails} Tails"

def coin_flip_sequence_sum(tries):
    """Prints the results of coin flips and the totals of the results"""
    return output_results([choice([0, 1]) for _ in range(0, tries)], sum)

def coin_flip_sequence_reduce(tries):
    """Prints the results of coin flips and the totals of the results"""
    return output_results([choice([0, 1]) for _ in range(0, tries)], lambda x: reduce(add, x, 0))

if __name__ == "__main__": #pragma: no cover
    main({
        "sum": coin_flip_sequence_sum,
        "reduce": coin_flip_sequence_reduce,
        "compare": compare
    }, int, lambda x: x >= 1, "How many coins to flip?")
