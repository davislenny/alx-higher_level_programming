#!/usr/bin/python3
"""
The '10-square' module
Defines class 'Square'
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Initiate the class"""
    def __init__(self, size):
        """Constructor"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """returns the are of the square"""
        return self.__size ** 2

    def __str__(self):
        """returns [Square] <width>/<height>"""
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
