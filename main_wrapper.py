"""Helper module for interactive execution"""

def main_no_args(funs):
    """Main method without extra arguments"""
    print("What subfunction would you like to do?")
    subf = input("Options: " + str([f for f, _ in funs.items()]) + "\n")
    if subf in funs.keys():
        print(funs[subf]())
    else:
        raise Exception

def main_one_arg(funs, prompt):
    """Main method for one argument functions"""
    print("What subfunction would you like to do?")
    subf = input("Options: " + str([f for f, _ in funs.items()]) + "\n")
    if subf in funs.keys():
        print(funs[subf](int(input(prompt + ":\n"))))
    else:
        raise Exception

def main_with_compare_and_arg(funs, prompt):
    """Main method for a module when there is a compare subfunction"""
    print("What subfunction would you like to do?")
    subf = input("Options: " + str([f for f, _ in funs.items()]) + "\n")
    if subf == "compare":
        comp_fun = funs.pop("compare")
        print(comp_fun(funs, int(input(prompt + ":\n"))))
    elif subf in funs.keys():
        print(funs[subf](int(input(prompt + ":\n"))))
    else:
        raise Exception
