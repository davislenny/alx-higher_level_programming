#!/usr/bin/python3
"""
The '1-write_file' module
Opens and writes a string to a text file (UTF8)
and returns the number of characters written
"""


def write_file(filename="", text=""):
    """function definition"""
    with open(filename, mode='w', encoding='utf-8') as fd:
        return fd.write(text)
