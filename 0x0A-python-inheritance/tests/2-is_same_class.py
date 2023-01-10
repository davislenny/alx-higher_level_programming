#!/usr/bin/python3
"""
This module defines the '2-is_same_class' function
"""


def is_same_class(obj, a_class):
    """
    This function returs true if object 'obj' is
    exactly an instance of class 'a_class'
    otherwise false
    """
    return type(obj) == a_class
