#!/usr/bin/env python3

"""Computes the factorial of input numbers and compares its compute time across algorithms"""

from timeit import default_timer as timer
from main_wrapper import main_with_compare_and_arg as main

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

def compare_factorials(funs, number):
    """Compares the times to compute the factorial of a number"""
    attempts = int(input("Attempts:\n"))
    times = {s: 0 for s, _ in funs.items()}
    for _ in range(attempts):
        for s, f in funs.items():
            time = -timer()
            f(number)
            time += timer()
            times[s] += time
    return "".join(["Average " + s + " time: " + str(t) + "\n" for s, t in times.items()])

if __name__ == "__main__":
    main({
        "iterative": iterative_factorial,
        "recursive": recursive_factorial, 
        "tail": tail_factorial, 
        "compare": compare_factorials
        },"Number")
