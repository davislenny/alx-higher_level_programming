#!/usr/bin/python3
"""
This module defines the 'inherits_from' function
"""


def inherits_from(obj, a_class):
    """
    Returns true if object 'obj' is a true subclass of
    a class 'a_class' otherwise false
    """
    return isinstance(obj, a_class) and type(obj) != a_class
