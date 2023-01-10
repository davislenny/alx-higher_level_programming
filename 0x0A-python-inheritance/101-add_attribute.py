#!/usr/bin/python3
"""
The '101-add_attribute'
Adds a new attribute to an object
"""


def add_attr(obj, attr, value):
    """add an attribute is possible"""
    if ('__dict__' in dir(obj)):
        setattr(obj, attr, value)

    else:
        raise TypeError("can't add new attribute")
