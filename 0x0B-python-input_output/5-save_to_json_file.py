#!/usr/bin/python3
"""
The '5-save_to_json_file' module
Writes an Object to a text file, using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """Functon definition"""
    with open(filename, mode='w', encoding='utf-8') as fd:
        json.dump(my_obj, fd)
