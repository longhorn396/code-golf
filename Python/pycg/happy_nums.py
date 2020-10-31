#!/usr/bin/env python3

"""Finds 'Happy' numbers. Numbers are happy if the sum of the squares of their digits equals 1.
Numbers are also happy if that sum is happy, and so on."""

from itertools import count
from .common import main_subf as main

def is_happy(num):
    """Process of finding happy numbers"""
    eval_set = set()
    while num not in eval_set and num > 0:
        num_string = str(num)
        squares = [pow(int(i), 2) for i in num_string]
        num_sum = sum(squares)
        if num_sum != 1:
            eval_set.add(num)
            num = num_sum
        else:
            return True
    return False

def search(wanted):
    """Returns a list of happy numbers"""
    happy_nums = []
    counter = count(1, 1)
    while len(happy_nums) < wanted:
        num = next(counter)
        if is_happy(num):
            happy_nums.append(num)
    return happy_nums

if __name__ == "__main__": # pragma: no cover
    main({"search": search, "eval": is_happy}, int, lambda x: x > 0, "Number")
