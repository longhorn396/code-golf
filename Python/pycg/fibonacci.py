#!/usr/bin/env python3

"""Computes the fibonacci sequence to the nth number and compares compute time across algorithms"""

from .common import main_subf as main
from .common import compare_subfs as compare

def dumb_fibonacci(n, seq=None):
    """Dumb solution"""
    if n <= 1:
        return 1, 0, [0]
    if n == 2:
        return 2, 1, [0, 1]
    result1 = dumb_fibonacci(n - 1)
    result2 = dumb_fibonacci(n - 2)
    seq = result1[2]
    seq.append(result1[1] + result2[1])
    return n, seq[n - 1], seq[:n]

def less_dumb_fibonacci(n, seq=None):
    """Slight improvement on the dumb_fibonacci"""
    if n <= 1:
        return 1, 0, [0]
    if n == 2:
        return 2, 1, [0, 1]
    result = dumb_fibonacci(n - 1)
    seq = result[2]
    seq.append(seq[-1] + seq[-2])
    return n, seq[n - 1], seq[:n]

def iterative_fibonacci(n):
    """Iterative solution"""
    seq = [0, 1]
    if n in seq:
        return n, seq[n - 1], seq[:n]
    while n > len(seq):
        seq.append(seq[-1] + seq[-2])
    return n, seq[-1], seq

def recursive_fibonacci(n, seq=None):
    """Recursive solution"""
    if seq is None:
        seq = [0, 1]
    if n > len(seq):
        seq.append(seq[-1] + seq[-2])
        return recursive_fibonacci(n, seq)
    return n, seq[n - 1], seq[:n]

if __name__ == "__main__": # pragma: no cover
    main({
        "dumb": dumb_fibonacci,
        "less_dumb": less_dumb_fibonacci,
        "iterative": iterative_fibonacci,
        "recursive": recursive_fibonacci,
        "compare": compare
    }, int, lambda x: x >= 1, "Number")
