#!/usr/bin/python3
"""
The '8-rectangle' module
Defines the class 'Rectangle'
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Initiate the class"""
    def __init__(self, width, height):
        """Constructor"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

        def area(self):
            """Implementing area: area of the rectangle"""
            return self.__width * self.__height

        def __str__(self):
            """returns [Rectangle] <width>/<height>"""
            return "[{:s}] {:d}/{:d}".format(self.__class__.__name__,
                                                self.__width, self.__height)
