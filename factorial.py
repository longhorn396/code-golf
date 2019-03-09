#!/usr/bin/env python3

from timeit import default_timer as timer

def factorial(num):
    """Recursive solution"""
    if num >= 2:
        return num * factorial(num - 1)
    else:
        return 1

def tail_factorial(num, result=1):
    """Tail-recursive solution"""
    if num >= 2:
        return tail_factorial(num - 1, num * result)
    else:
        return result

def compare_factorials(number):
    attempts = int(input("Attempts:\n"))
    rec_tot = 0.0
    tail_tot = 0.0
    for _ in range(attempts):
        rec_tot -= timer()
        recursive = factorial(number)
        rec_tot += timer()
        tail_tot -= timer()
        tail = tail_factorial(number, 1)
        tail_tot += timer()
        assert recursive == tail
    return "Average Recursive time:\t\t{}\nAverage Tail-recursive time:\t{}".format(rec_tot /\
        attempts, tail_tot / attempts)

if __name__ == "__main__":
    funs = {"recursive": factorial, "tail": tail_factorial, "compare": compare_factorials}
    print("What subfunction would you like to do?")
    subf = input("Options: " + str([f for f, _ in funs.items()]) + "\n")
    if subf in funs.keys():
        print(funs[subf](int(input("Number:\n"))))
    else:
        raise Exception
