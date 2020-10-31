"""Helper module for execution and other common functionality"""

import sys
import traceback
from timeit import default_timer as timer

def _my_exception_handler(ex_type, value, trace_back): # pragma: no cover
    """Exception handler that outputs minimal information for basic Exceptions"""
    print(value)
    if str(ex_type) != "<class 'Exception'>":
        traceback.print_tb(trace_back)

def use_custom_exception_handler(): # pragma: no cover
    """Redefine the system's exception handler"""
    sys.excepthook = _my_exception_handler

def main(fun, trans, *prompts): # pragma: no cover
    """Main method when a module only has one function"""
    use_custom_exception_handler()
    if len(sys.argv) > 1:
        args = [trans(arg) for arg in sys.argv[1:]]
    else:
        args = [trans(input(p + ":\n")) for p in prompts]
    try:
        print(fun(*args))
    except AssertionError:
        print("Make sure you pass in valid arguments")

def compare_subfs(funs, attempts, args): # pragma: no cover
    """Compares the execution times of functions in this module"""
    spaces = max([len(subf_name) for subf_name in funs.keys()])
    times = {subf_name: 0 for subf_name in funs.keys()}
    for _ in range(attempts):
        for subf_name, subf in funs.items():
            time = -timer()
            subf(*args)
            time += timer()
            times[subf_name] += time / attempts
    return "".join([f"{subf_name: <{spaces}} average: {t:.15f}\n"\
        for subf_name, t in times.items()])

def main_subf(funs, trans, check, *prompts): # pragma: no cover
    """Main method when subfunctions are involved"""
    use_custom_exception_handler()
    if len(sys.argv) > 1:
        subf = sys.argv[1]
    else:
        print("What subfunction would you like to do?")
        subf = input("Options: " + str(funs.keys()) + "\n")
    if subf in funs.keys():
        if len(sys.argv) > 2:
            args = [trans(arg) for arg in sys.argv[2:]]
        else:
            args = [trans(input(p + ":\n")) for p in prompts]
        if all([check(arg) for arg in args]):
            if subf == "compare":
                print(funs.pop("compare")(funs, int(input("Attempts:\n")), args))
            else:
                print(funs[subf](*args))
        else:
            raise Exception("Make sure you pass in valid arguments")
    else:
        raise Exception("Make sure you pass in a valid subfunction")
