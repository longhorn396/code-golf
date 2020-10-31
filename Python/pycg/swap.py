#!/usr/bin/env python3

"""Different ways to swap numbers.
I was under the impression that swapping with xor was the fastest and wrote this to test"""

from .common import main_subf as main
from .common import compare_subfs as compare

def temp_swap(x, y):
    """Swap with a temp variable"""
    temp = x # pylint: disable=consider-swap-variables
    x = y
    y = temp
    return x, y

def temp2_swap(x, y):
    """temp_swap with one less assignment"""
    temp = x
    x = y
    return x, temp

def tuple_swap(x, y):
    """Swap with tuple unpacking"""
    (x, y) = (y, x)
    return x, y

def return_swap(x, y):
    """Swap with tuple unpacking on return"""
    return y, x

def xor_swap(x, y):
    """Swap with exclusive or"""
    x = x ^ y
    y = x ^ y
    x = x ^ y
    return x, y

if __name__ == "__main__": # pragma: no cover
    main({
        "temp": temp_swap,
        "temp2": temp2_swap,
        "tuple": tuple_swap,
        "return": return_swap,
        "xor": xor_swap,
        "compare": compare
    }, int, lambda x: True, "Number 1", "Number 2")
