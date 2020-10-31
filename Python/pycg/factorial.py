#!/usr/bin/env python3

"""Computes the factorial of input numbers and compares its compute time across algorithms"""

from math import factorial as imported
from functools import reduce
from operator import mul
from .common import main_subf as main
from .common import compare_subfs as compare

def for_factorial(num):
    """Iterative solution"""
    result = 1
    for i in range(2, num + 1):
        result *= i
    return result

def while_factorial(num):
    """Solution with while loop"""
    result = 1
    while num > 1:
        result *= num
        num -= 1
    return result

def recursive_factorial(num):
    """Recursive solution"""
    if num >= 2:
        return num * recursive_factorial(num - 1)
    return 1

def tail_factorial(num, result=1):
    """Tail-recursive solution"""
    if num >= 2:
        return tail_factorial(num - 1, num * result)
    return result

def range_factorial(num):
    """Solution that iterates over a range"""
    result = 1
    i = iter(range(1, num + 1))
    try:
        while True:
            result *= next(i)
    except StopIteration:
        pass
    return result

def reduce1_factorial(num):
    """Solution that uses reduce and a lambda"""
    return reduce(lambda x, y: x * y, range(1, num + 1), 1)

def reduce2_factorial(num):
    """Solution that uses reduce and the mul operator"""
    return reduce(mul, range(1, num + 1), 1)

if __name__ == "__main__": #pragma: no cover
    main({
        "imported": imported,
        "for_loop": for_factorial,
        "while_loop": while_factorial,
        "recursive": recursive_factorial,
        "tail": tail_factorial,
        "range_iter": range_factorial,
        "reduce1": reduce1_factorial,
        "reduce2": reduce2_factorial,
        "compare": compare
    }, int, lambda x: 0 <= x < 996, "Number")
