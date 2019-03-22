#!/usr/bin/env python3

"""Used to convert Python strings of JSON into human-readable JSON"""

from ast import literal_eval
from common import main

def py_to_js(obj_str):
    """Evaluate string and return readable result"""
    return rprint(literal_eval(obj_str))

def rprint(obj, tabs=0):
    """Make 'obj' human readable in JSON context"""
    def remove_last_comma(parsed):
        last_comma_index = parsed.rfind(",")
        if last_comma_index > 0:
            return parsed[:last_comma_index] + parsed[last_comma_index + 1:]
        return parsed
    parsed = ""
    if isinstance(obj, dict):
        tabs += 1
        parsed += "{\n"
        for k, v in obj.items():
            parsed += "".join(["    "] * tabs) + rprint(k, tabs) + ": " + rprint(v, tabs) + ",\n"
        tabs -= 1
        parsed += "".join(["    "] * tabs) + "}"
        parsed = remove_last_comma(parsed)
    elif isinstance(obj, list):
        tabs += 1
        parsed = "[\n"
        for i in obj:
            parsed += "".join(["    "] * tabs) + rprint(i, tabs) + ",\n"
        tabs -= 1
        parsed += "".join(["    "] * tabs) + "]"
        parsed = remove_last_comma(parsed)
    elif isinstance(obj, str):
        return parsed + '"' + obj + '"'
    elif isinstance(obj, bool):
        return ["false", "true"][obj]
    elif isinstance(obj, (int, float)):
        return str(obj)
    else:
        raise Exception(f"Unexpected type: {type(obj)}")
    return parsed.replace("'", '"')

if __name__ == "__main__":
    main(py_to_js, str, "Object to convert")
