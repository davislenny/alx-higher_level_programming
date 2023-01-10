#!/usr/bin/python3
"""
The '4-from_json_string' module
Returns an object (Python data structure) represented
by a JSON string
"""
import json


def from_json_string(my_str):
    """Functon definition"""
    return json.loads(my_str)
