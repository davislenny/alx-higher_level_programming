#!/usr/bin/python3
"""
The '5-base_geometry' module
Defines an empty class
"""


class BaseGeometry:
    """Function definition"""
    def area(self):
        """Empty function Raises an exception"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """validates value"""
        if type(value) != int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
