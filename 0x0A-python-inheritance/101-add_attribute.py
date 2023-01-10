#!/usr/bin/python3
"""
The '101-add_attribute'
Adds a new attribute to an object
"""


def add_attribute(obj, name, value):
    """add an attribute is possible"""
    if hasattr(obj, "__dict__") or
        (hasattr(obj, "__slots__") and name in obj.__slots__):
        setattr(obj, name, value)

    else:
        raise TypeError("can't add new attribute")
