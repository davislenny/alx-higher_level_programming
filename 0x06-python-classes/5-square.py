#!/usr/bin/python3
"""Initiate a class"""


class Square:
    """Define the class
    check for errors
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    @property
    def size(self):
        """get/retrieve size"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets size value"""
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """finds the area of a square"""
        return self.__size ** 2

    def my_print(self):
        """prints the square with the character #"""
        print("\n".join(["#" * self.__size for rows in range(self.__size)]))
