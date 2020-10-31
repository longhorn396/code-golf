"""Helper module for execution and other common functionality"""

def _my_exception_handler(ex_type, value, tb): # pragma: no cover
    """Exception handler that outputs minimal information for basic Exceptions"""
    print(value)
    if str(ex_type) != "<class 'Exception'>":
        import traceback
        traceback.print_tb(tb)

def use_custom_exception_handler(): # pragma: no cover
    """Redefine the system's exception handler"""
    import sys
    sys.excepthook = _my_exception_handler

def main(fun, trans, *prompts): # pragma: no cover
    """Main method when a module only has one function"""
    from sys import argv
    use_custom_exception_handler()
    if len(argv) > 1:
        args = [trans(arg) for arg in argv[1:]]
    else:
        args = [trans(input(p + ":\n")) for p in prompts]
    try:
        print(fun(*args))
    except AssertionError:
        print("Make sure you pass in valid arguments")

def compare_subfs(funs, attempts, args): # pragma: no cover
    """Compares the execution times of functions in this module"""
    from timeit import default_timer as timer
    spaces = max([len(s) for s in funs.keys()])
    times = {s: 0 for s in funs.keys()}
    for _ in range(attempts):
        for s, f in funs.items():
            time = -timer()
            f(*args)
            time += timer()
            times[s] += time / attempts
    return "".join([f"{s: <{spaces}} average: {t:.15f}\n" for s, t in times.items()])

def main_subf(funs, trans, check, *prompts): # pragma: no cover
    """Main method when subfunctions are involved"""
    from sys import argv
    use_custom_exception_handler()
    if len(argv) > 1:
        subf = argv[1]
    else:
        print("What subfunction would you like to do?")
        subf = input("Options: " + str([f for f in funs.keys()]) + "\n")
    if subf in funs.keys():
        if len(argv) > 2:
            args = [trans(arg) for arg in argv[2:]]
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
