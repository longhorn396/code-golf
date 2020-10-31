#!/usr/bin/env python3

"""Different ways to swap numbers.
I was under the impression that swapping with xor was the fastest and wrote this to test"""

from .common import main_subf as main
from .common import compare_subfs as compare

def temp_swap(i, j):
    """Swap with a temp variable"""
    temp = i # pylint: disable=consider-swap-variables
    i = j
    j = temp
    return i, j

def temp2_swap(i, j):
    """temp_swap with one less assignment"""
    temp = i
    i = j
    return i, temp

def tuple_swap(i, j):
    """Swap with tuple unpacking"""
    (i, j) = (j, i)
    return i, j

def return_swap(i, j):
    """Swap with tuple unpacking on return"""
    return j, i

def xor_swap(i, j):
    """Swap with exclusive or"""
    i = i ^ j
    j = i ^ j
    i = i ^ j
    return i, j

if __name__ == "__main__": # pragma: no cover
    main({
        "temp": temp_swap,
        "temp2": temp2_swap,
        "tuple": tuple_swap,
        "return": return_swap,
        "xor": xor_swap,
        "compare": compare
    }, int, lambda x: True, "Number 1", "Number 2")
