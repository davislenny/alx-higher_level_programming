#!/usr/bin/python3
"""
The '3-to_json_string' module
Returns the JSON representation of an object (string)
"""
import json


def to_json_string(my_obj):
    """Function definition"""
    return json.dumbs(my_obj)
