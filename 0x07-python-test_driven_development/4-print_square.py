#!/usr/bin/python3
"""
The 'print_square' module
Defines a funtion to print a square
"""


def print_square(size):
    """
    This function prints a square of size 'size'
    with the character #
    Raises:
        TypeError if size is not an int
        ValueError if size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    print("\n".join(["#" * size for rows in range(size)]))
