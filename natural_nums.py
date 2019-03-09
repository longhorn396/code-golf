#!/usr/bin/env python3

"""Finds the nth natural number"""

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
    return "The natural number is {} in {}".format(res_str[n-1], res_str[m[n][0]:m[n][1]])

if __name__ == "__main__":
    print(find_nth_natural_number(int(input("Which natural number?\n")),\
        int(input("How big a range?\n"))))
