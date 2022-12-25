#!/usr/bin/python3
"""Initiate a class named Square"""


class Square:
    """
    Define class
    var:
        size: square size of type int
    """

    def __init__(self, size=0):
        """
        Check for errors
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
    """
    Method that returns area of
    the square
    """
        return (self.__size * self.__size)
