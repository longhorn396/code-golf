#!/usr/bin/env python3

"""Simple Reverse Polish Notation calculators"""

from operator import add, sub, mul, floordiv, mod
from .common import main_subf as main
from .common import compare_subfs as compare

ops = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": floordiv,
    "%": mod
}

def iterative_rpn(stack):
    """Iterative solution"""
    operands = []
    for item in stack.split():
        if item.isnumeric():
            operands.append(int(item))
        else:
            operands.append(ops[item](operands.pop(), operands.pop()))
    assert len(operands) == 1
    return operands.pop()

def recursive_rpn_wrap(stack):
    """Wrapper for recursive solution"""
    return recursive_rpn(stack.split())

def recursive_rpn(stack):
    """Recursive solution"""
    item = stack.pop()
    if item.isnumeric():
        return int(item)
    return ops[item](recursive_rpn(stack), recursive_rpn(stack))

if __name__ == "__main__": # pragma: no cover
    main({
        "for_loop": iterative_rpn,
        "recursive": recursive_rpn_wrap,
        "compare": compare}, str, lambda x: True, "RPN Stack")
