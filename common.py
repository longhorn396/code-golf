"""Helper module for interactive execution and other common functionality"""

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
    use_custom_exception_handler()
    args = [trans(input(p + ":\n")) for p in prompts]
    try:
        print(fun(*args))
    except AssertionError:
        print("Make sure you pass in valid arguments")

def compare_subfs(funs, tries): # pragma: no cover
    """Compares the execution times of functions in this module"""
    from timeit import default_timer as timer
    spaces = max([len(s) for s in funs.keys()])
    times = {s: 0 for s in funs.keys()}
    attempts = int(input("Attempts:\n"))
    for _ in range(attempts):
        for s, f in funs.items():
            time = -timer()
            f(tries)
            time += timer()
            times[s] += time / attempts
    return "".join([f"{s: <{spaces}} average: {t:.15f}\n" for s, t in times.items()])

def main_subf(funs, trans, check, *prompts): # pragma: no cover
    """Main method when subfunctions are involved"""
    use_custom_exception_handler()
    print("What subfunction would you like to do?")
    subf = input("Options: " + str([f for f in funs.keys()]) + "\n")
    if subf in funs.keys():
        args = [trans(input(p + ":\n")) for p in prompts]
        if all([check(arg) for arg in args]):
            if subf == "compare":
                comp_fun = funs.pop("compare")
                print(comp_fun(funs, *args))
            else:
                print(funs[subf](*args))
        else:
            raise Exception("Make sure you pass in valid arguments")
    else:
        raise Exception("Make sure you pass in a valid subfunction")
