#!/usr/bin/env python

"""Finds 'Happy' numbers. Numbers are happy if the sum of the squares of their digits equals 1.
Numbers are also happy if that sum is happy, and so on."""

from sys import argv
from itertools import count

def is_happy(num):
    """Process of finding happy numbers"""
    eval_set = set()
    while num not in eval_set:
        num_string = str(num)
        squares = [pow(int(i), 2) for i in num_string]
        num_sum = sum(squares)
        if num_sum != 1:
            eval_set.add(num)
            num = num_sum
        else:
            return True
    return False

if __name__ == "__main__":
    if len(argv) == 1 or argv[1] == "search":
        try:
            WANTED = int(argv[2])
        except IndexError:
            WANTED = 12
        HAPPYS = []
        COUNT = count(1, 1)
        while len(HAPPYS) < WANTED:
            NUM = next(COUNT)
            if is_happy(NUM):
                HAPPYS.append(NUM)
        print(HAPPYS)
    elif argv[1] == "eval":
        print(is_happy(int(argv[2])))
