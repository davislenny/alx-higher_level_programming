#!/usr/bin/python3
"""Initiate a new Class"""


class Square:
    """Define the class
    Initiate var: size
    size: squar size of type int"""

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """returs the area of the square"""
        return self.__size**2

    @property
    def size(self):
        """gets/retrieve size"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets the size value"""
        self.__size = value
