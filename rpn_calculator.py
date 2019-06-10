#!/usr/bin/env python3

"""Simple Reverse Polish Notation calculators"""

from operator import add, sub, mul, floordiv, mod
from common import main_subf as main
from common import compare_subfs as compare

ops = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": floordiv,
    "%": mod
}

def iterative(stack):
    """Iterative solution"""
    operands = []
    for item in stack.split():
        if item.isnumeric():
            operands.append(int(item))
        else:
            operands.append(ops[item](operands.pop(), operands.pop()))
    assert len(operands) == 1
    return operands.pop()

def recursive_wrap(stack):
    """Wrapper for recursive recursive solution"""
    return recursive(stack.split())

def recursive(stack):
    """recursive recursive solution"""
    item = stack.pop()
    if item.isnumeric():
        return int(item)
    return ops[item](recursive(stack), recursive(stack))

if __name__ == "__main__": # pragma: no cover
    main({
        "for_loop": iterative,
        "recursive": recursive_wrap,
        "compare": compare}, str, lambda x: True, "RPN Stack")
