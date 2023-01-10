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
