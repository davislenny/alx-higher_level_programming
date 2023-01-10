#!/usr/bin/python3
"""
The '6-load_from_json_file' module
Creates an Object from a “JSON file”
"""
import json


def load_from_json_file(filename):
    """Function definition"""
    with open(filename, mode='r', encoding='utf-8') as fd:
        return json.load(fd)
