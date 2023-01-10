#!/usr/bin/python3
"""
The '2-append_write' module
Opens and appends a string at the end of a text file
and returns the number of characters added
"""


def append_write(filename="", text=""):
    """Function definition"""
    with open(filename, mode='a', encoding='utf-8') as fd:
        return fd.append(text)
