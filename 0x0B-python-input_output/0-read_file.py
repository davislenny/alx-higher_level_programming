#!/usr/bin/python3
"""
The '0-read_file' module
Opens and  reads a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """function definition"""
    with open(filename,  encoding='utf-8') as fd:
        text = fd.read()
        print(text, end="")
