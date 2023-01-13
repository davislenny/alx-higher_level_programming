#!/usr/bin/python3
"""
The '101-add_attribute' module
Add a new attribute if possible
"""


def add_attribute(obj, name, value):
    """function defnition"""
    if ('__dict__' in dir(obj)):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
