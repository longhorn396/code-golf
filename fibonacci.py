#!/usr/bin/env python3

"""Computes the fibonacci sequence to the nth number and compares compute time across algorithms"""

from common import main_subf as main
from common import compare_subfs as compare

def dumb_fibonacci(n):
    """Dumb solution; Returns only the Nth number"""
    if n < 2:
        return n
    return dumb_fibonacci(n - 1) + dumb_fibonacci(n - 2)

def iterative_fibonacci(n):
    """Iterative solution; Returns N, the Nth number, and the sequence up to N"""
    seq = [0, 1]
    if n in seq:
        return n, seq[n - 1], seq[:n]
    while n > len(seq):
        seq.append(seq[-1] + seq[-2])
    return n, seq[-1], seq

def recursive_fibonacci(n, seq=None):
    """Recursive solution; Returns N, the Nth number, and the sequence up to N"""
    if seq is None:
        seq = [0, 1]
    if n > len(seq):
        seq.append(seq[-1] + seq[-2])
        return recursive_fibonacci(n, seq)
    return n, seq[n - 1], seq[:n]

if __name__ == "__main__": # pragma: no cover
    main({
        "dumb": dumb_fibonacci,
        "iterative": iterative_fibonacci,
        "recursive": recursive_fibonacci,
        "compare": compare
    }, int, lambda x: x >= 1, "Number")
