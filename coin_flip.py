#!/usr/bin/env python3

"""Generates a sequence of coin flips"""

from timeit import default_timer as timer
from random import choice
from functools import reduce
from operator import add
from common import main_with_compare_and_arg as main

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

def compare(funs, tries):
    """Compares the execution times of functions in this module"""
    times = {s: 0 for s, _ in funs.items()}
    attempts = int(input("Attempts:\n"))
    for _ in range(attempts):
        for s, f in funs.items():
            time = -timer()
            f(tries)
            time += timer()
            times[s] += time / attempts
    return "".join(["{:6s} average: {:.15f}\n".format(s, t) for s, t in times.items()])

if __name__ == "__main__":
    main({
        "sum": coin_flip_sequence_sum,
        "reduce": coin_flip_sequence_reduce,
        "compare": compare
    }, "How many coins to flip?", int, lambda x: x >= 1)
