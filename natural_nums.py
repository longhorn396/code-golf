#!/usr/bin/env python3

"""Finds the nth natural number"""

from common import main

def find_nth_natural_number(n, limit):
    """Returns the nth natural number and the number containing it"""
    assert n >= 1
    m = {}
    nums = []
    prev_len = 0
    for i in range(1, limit + 1):
        nums.append(i)
        new_len = len(str(i)) + prev_len
        m.update({j: (prev_len, new_len) for j in range(prev_len + 1, new_len + 1)})
        if new_len >= n:
            break
        prev_len = new_len
    res_str = "".join(str(i) for i in nums)
    assert n <= len(res_str)
    return f"The natural number is {res_str[n-1]} in {res_str[m[n][0]:m[n][1]]}"

if __name__ == "__main__": # pragma: no cover
    main(find_nth_natural_number, int, "Which natural number?", "How big a range?")
