#!/usr/bin/python3
"""Initiate class named Square"""

class Square:
    """
    Define class
    var:
        size: square size of type int
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

"""Define a Public instance method
    that returns the area of the square"""


        def area(self):
            return self.__size**2
