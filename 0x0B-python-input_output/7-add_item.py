#!/usr/bin/python3
"""
The '7-add_item' module
Adds all arguments to a Python list, and then
save them to 'add_item.json' file
"""
from sys import argv
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = "add_item.json"

try:
    List = load_from_json_file(filename)
except FileNotFoundError:
    List = []

save_to_json_file(List + argv[1:], filename)
