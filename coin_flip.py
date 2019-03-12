#!/usr/bin/env python3

"""Generates a sequence of coin flips"""

from random import choice
from functools import reduce
from operator import add
from common import main_with_compare_and_arg as main
from common import compare_subfs as compare

def coin_flip_sequence_sum(tries):
    """Prints the results of coin flips and the totals of the results"""
    results = [choice([0, 1]) for _ in range(0, tries)]
    tails = sum(results)
    heads = len(results) - tails
    result = ", ".join([["Heads", "Tails"][flip] for flip in results])
    return result + "\n{:d} Heads; {:d} Tails".format(heads, tails)

def coin_flip_sequence_reduce(tries):
    """Prints the results of coin flips and the totals of the results"""
    results = [choice([0, 1]) for _ in range(0, tries)]
    tails = reduce(add, results, 0)
    heads = len(results) - tails
    result = ", ".join([["Heads", "Tails"][flip] for flip in results])
    return result + "\n{:d} Heads; {:d} Tails".format(heads, tails)

if __name__ == "__main__":
    main({
        "sum": coin_flip_sequence_sum,
        "reduce": coin_flip_sequence_reduce,
        "compare": compare
    }, "How many coins to flip?", int, lambda x: x >= 1)
