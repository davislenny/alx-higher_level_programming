#!/usr/bin/python3
"""
This is the "addition" module
This module contains the addition function that adds two
integers.
"""


def add_integer(a, b=98):
    """
    Returns the integer addition of a and b
    Raises TypeError if either a or b is not int or float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
