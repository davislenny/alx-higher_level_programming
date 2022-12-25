#!/usr/bin/python3
"""Initiate a class named Square"""


class Square:
    """Define class square"""

    def __init__(self, size=0):
        """
        Check for type in size value
        Raise errors occurred
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """Find area of the squar
        Returns size squared
        """
        return self.__size ** 2
