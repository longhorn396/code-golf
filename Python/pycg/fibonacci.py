#!/usr/bin/env python3

"""Computes the fibonacci sequence to the nth number and compares compute time across algorithms"""

from .common import main_subf as main
from .common import compare_subfs as compare

def dumb_fibonacci(i, seq=None):
    """Dumb solution"""
    if i <= 1:
        return 1, 0, [0]
    if i == 2:
        return 2, 1, [0, 1]
    result1 = dumb_fibonacci(i - 1)
    result2 = dumb_fibonacci(i - 2)
    seq = result1[2]
    seq.append(result1[1] + result2[1])
    return i, seq[i - 1], seq[:i]

def less_dumb_fibonacci(i, seq=None):
    """Slight improvement on the dumb_fibonacci"""
    if i <= 1:
        return 1, 0, [0]
    if i == 2:
        return 2, 1, [0, 1]
    result = dumb_fibonacci(i - 1)
    seq = result[2]
    seq.append(seq[-1] + seq[-2])
    return i, seq[i - 1], seq[:i]

def iterative_fibonacci(i):
    """Iterative solution"""
    seq = [0, 1]
    if i in seq:
        return i, seq[i - 1], seq[:i]
    while i > len(seq):
        seq.append(seq[-1] + seq[-2])
    return i, seq[-1], seq

def recursive_fibonacci(i, seq=None):
    """Recursive solution"""
    if seq is None:
        seq = [0, 1]
    if i > len(seq):
        seq.append(seq[-1] + seq[-2])
        return recursive_fibonacci(i, seq)
    return i, seq[i - 1], seq[:i]

if __name__ == "__main__": # pragma: no cover
    main({
        "dumb": dumb_fibonacci,
        "less_dumb": less_dumb_fibonacci,
        "iterative": iterative_fibonacci,
        "recursive": recursive_fibonacci,
        "compare": compare
    }, int, lambda x: x >= 1, "Number")
