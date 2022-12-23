#!/usr/bin/python3
def safe_function(fct, *args):
    from sys import stderr
    try:
        return fct(*args)
    except Exceptions as exc:
        stderr.write("Exception: {}\n".format(exc))
        return None
