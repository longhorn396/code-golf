"""Helper module for interactive execution and other common functionality"""

def _my_exception_handler(ex_type, value, tb):
    """Exception handler that outputs minimal information for basic Exceptions"""
    print(value)
    if str(ex_type) != "<class 'Exception'>":
        import traceback
        traceback.print_tb(tb)

def use_custom_exception_handler():
    """Redefine the system's exception handler"""
    import sys
    sys.excepthook = _my_exception_handler

def main_no_args(funs):
    """Main method without extra arguments"""
    print("What subfunction would you like to do?")
    subf = input("Options: " + str([f for f, _ in funs.items()]) + "\n")
    if subf in funs.keys():
        print(funs[subf]())
    else:
        raise Exception("Make sure you pass in valid arguments")

def main_one_arg(funs, prompt, trans=int, check=lambda x: True):
    """Main method for one argument functions"""
    print("What subfunction would you like to do?")
    subf = input("Options: " + str([f for f, _ in funs.items()]) + "\n")
    param = trans(input(prompt + ":\n"))
    if subf in funs.keys() and check(param):
        print(funs[subf](param))
    else:
        raise Exception("Make sure you pass in valid arguments")

def main_with_compare(funs):
    """Main method for a module when there is a compare subfunction"""
    print("What subfunction would you like to do?")
    subf = input("Options: " + str([f for f, _ in funs.items()]) + "\n")
    if subf == "compare":
        comp_fun = funs.pop("compare")
        print(comp_fun(funs))
    elif subf in funs.keys():
        print(funs[subf]())
    else:
        raise Exception("Make sure you pass in valid arguments")

def main_with_compare_and_arg(funs, prompt, trans=int, check=lambda x: True):
    """Main method for a module when there is a compare subfunction"""
    use_custom_exception_handler()
    print("What subfunction would you like to do?")
    subf = input("Options: " + str([f for f, _ in funs.items()]) + "\n")
    param = trans(input(prompt + ":\n"))
    if subf == "compare" and check(param):
        comp_fun = funs.pop("compare")
        print(comp_fun(funs, param))
    elif subf in funs.keys() and check(param):
        print(funs[subf](param))
    else:
        raise Exception("Make sure you pass in valid arguments")
