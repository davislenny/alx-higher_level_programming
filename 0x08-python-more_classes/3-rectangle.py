#!/usr/bin/python3
"""
The '2-rectangle' module
Defines the class rectangle
"""


class Rectangle:
    """Initiate the class"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width = value"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('with must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Retireves the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets height = value"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """computes area of the rectangle"""
        return (self.width * self.height)

    def perimeter(self):
        """coputes the perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)
   
    def __str__(self):
       """returns the recatangle as the # character"""
       if self.width == 0 or self.height == 0:
           return ""
       return (self.height * ('#' * self.width + '\n'))[:-1]
