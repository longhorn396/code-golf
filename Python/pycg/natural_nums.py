#!/usr/bin/env python3

"""Finds the nth natural number"""

from .common import main

def find_nth_natural_number(i, limit):
    """Returns the ith natural number and the number containing it"""
    assert i >= 1
    number_map = {}
    nums = []
    prev_len = 0
    for num in range(1, limit + 1):
        nums.append(num)
        new_len = len(str(num)) + prev_len
        number_map.update({j: (prev_len, new_len) for j in range(prev_len + 1, new_len + 1)})
        if new_len >= i:
            break
        prev_len = new_len
    res_str = "".join(str(num) for num in nums)
    assert i <= len(res_str)
    return f"The natural number is {res_str[i-1]} in {res_str[number_map[i][0]:number_map[i][1]]}"

if __name__ == "__main__": # pragma: no cover
    main(find_nth_natural_number, int, "Which natural number?", "How big a range?")
