#!/usr/bin/python3
"""Initiate a class named Square"""


class Square:
    """
    size: length of the square
    area: area of the square
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initialize values of the square"""
        self.size = size
        self.position = position

    def area(self):
        """returns the area of square"""
        return self.__size ** 2

    @property
    def size(self):
        """returns the size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets the size of square to value"""
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def my_print(self):
        """prints the square with the character #"""
        print("\n".join(["#" * self.__size for rows in range(self._-size)]))

    @property
    def position(self):
        """returns the position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2 or \
        len([i for i in value if isinstance(i, int) and i >= 0]) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value
