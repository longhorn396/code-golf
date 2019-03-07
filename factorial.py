"""Computes the factorial of an integer"""

from sys import argv
from timeit import default_timer as timer

def factorial(num):
    """Recursive solution"""
    if num >= 2:
        return num * factorial(num - 1)
    else:
        return 1

def tail_factorial(num, result):
    """Tail-recursive solution"""
    if num >= 2:
        return tail_factorial(num - 1, num * result)
    else:
        return result

if __name__ == "__main__":
    if argv[1] == "tail":
        print(tail_factorial(int(argv[2]), 1))
    elif argv[1] == "recursive":
        print(factorial(int(argv[2])))
    else:
        number = int(argv[1])
        try:
            attempts = int(argv[2])
        except IndexError:
            attempts = 10
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
        print("Average Recursive time:\t\t{}".format(rec_tot / attempts))
        print("Average Tail-recursive time:\t{}".format(tail_tot / attempts))
