#!/usr/bin/python3
"""
Defines the 'is_kind_of_class' function
"""


def is_kind_of_class(obj, a_class):
    """
    Returns true if object 'obj' is an instance of
    or kind_of a class 'a_class'
    otherwise false
    """
    return isinstance(obj, a_class)
