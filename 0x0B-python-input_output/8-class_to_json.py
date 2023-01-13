#!/usr/bin/python3
"""
The '8-class_to_json' module
Returns the dictionary description with simple data structure
for JSON serialization of an object
"""


def class_to_json(obj):
    """function definition
        :obj is an instance of a class
    """
    if ('__dict__' in dir(obj)):
        return obj.__dict__.copy()
    else:
        return {}
