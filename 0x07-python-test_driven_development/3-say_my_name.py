#!/usr/bin/python3
"""
The 'say_my_name' module
The function defined herein prints:
    My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """
    first_name is the first name
    and last-name the last name
    Raises:
        TypeError if names are not of string type
    """
    if isinstance(first_name, str) and isinstance(last_name, str):
        print(f'My name is {first_name} {last_name}')
    else:
        raise TypeError("{:s} must be a string".
                        format("first_name" if isinstance(last_name, str)
                                else "last_name"))
