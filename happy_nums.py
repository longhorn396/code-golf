#!/usr/bin/env python

"""Finds 'Happy' numbers. Numbers are happy if the sum of the squares of their digits equals 1.
Numbers are also happy if that sum is happy, and so on."""

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

def search():
    try:
        wanted = int(input("How many happy numbers do you want to find?\n"))
    except ValueError:
        wanted = 12
    happy_nums = []
    counter = count(1, 1)
    while len(happy_nums) < wanted:
        num = next(counter)
        if is_happy(num):
            happy_nums.append(num)
    return happy_nums

def evaluate():
    return is_happy(int(input("Input a number for a happiness check\n")))

if __name__ == "__main__":
    funs = ["search", "eval"]
    subf = raw_input("What subfunction would you like to do?\n")
    print(subf)
    print(type(subf))
    if subf == "search":
        print(search())
    elif subf == "eval":
        print(evaluate())
    else:
        raise Exception