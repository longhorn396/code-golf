#!/usr/bin/env python3

"""Computes the factorial of input numbers and compares its compute time across algorithms"""

from timeit import default_timer as timer
from main_wrapper import main_one_arg as main

def iterative_factorial(num):
    """Iterative solution"""
    result = 1
    for i in range(2, num + 1):
        result *= i
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

def compare_factorials(number):
    """Compares the times to compute the factorial of a number"""
    attempts = int(input("Attempts:\n"))
    rec_tot = 0.0
    tail_tot = 0.0
    for _ in range(attempts):
        rec_tot -= timer()
        recursive = recursive_factorial(number)
        rec_tot += timer()
        tail_tot -= timer()
        tail = tail_factorial(number, 1)
        tail_tot += timer()
        assert recursive == tail
    return "Average Recursive time:\t\t{}\nAverage Tail-recursive time:\t{}".format(rec_tot /\
        attempts, tail_tot / attempts)

if __name__ == "__main__":
    main({
        "iterative": iterative_factorial,
        "recursive": recursive_factorial, 
        "tail": tail_factorial, 
        "compare": compare_factorials
        },"Number")
