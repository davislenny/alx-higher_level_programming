#!/usr/bin/python3
"""
The '2-rectangle' module
Defines the class rectangle
"""


class Rectangle:
    """Initiate the class"""
    number_of_instances = 0
    """initiate number of instances"""
    print_symbol = '#'
    """initiate any string symbol to print the rectangle"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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
        """Retrireves the height"""
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
        """returns the rectangle as the # character"""
        if self.width == 0 or self.height == 0:
            return ""
        return (self.height * (str(self.print_symbol) * self.width + '\n'))[:-1]

    def __repr__(self):
        """formal string representing the rectangle"""
        return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"

    def __del__(self):
        """deletes an instance"""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns a rectangle with the biggest area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        return rect_1

    @classmethod
    def square(cls, size=0):
        """returns new Rectangle instance with width == height == size"""
        return cls(size, size)
