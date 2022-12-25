#!/usr/bin/python3
"""Initiate a new Class"""


class Square:
    """Define the class
    Initiate var: size
    size: squar size of type int"""

    def __init__(self, size=0):

    @property
    def size(self):
        """gets/retrieve size"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets the size value
        rases error
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """returs the area of the square"""
        return self.size ** 2
