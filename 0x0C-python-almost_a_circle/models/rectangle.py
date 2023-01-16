#!/usr/bin/python3
""" rectangle module """
from models.base import Base


class Rectangle(Base):
    """ Class definition """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Constructor """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def integer_validate(self, name, value, flag=None):
        """ Validates value to type and range """
        if type(value) != int:
            raise TypeError('{} must be an integer'.format(name))
        if not flag and value < 0:
            raise ValueError('{} must be >= 0'.format(name))
        elif flag and value <= 0:
            raise ValueError('{} must be > 0'.format(name))

    @property
    def width(self):
        """ Returns the width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets the value of width to 'value' """
        self.integer_validate('width', value, 1)
        self.__width = value

    @property
    def height(self):
        """ Returns height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Sets the height to 'value' """
        self.integer_validate('height', value, 1)
        self.__height = value

    @property
    def x(self):
        """ Returns x """
        return self.__x

    @x.setter
    def x(self, value):
        """ Sets x to 'value' """
        self.integer_validate('x', value)
        self.__x = value

    @property
    def y(self):
        """ Returns y """
        return self.__y

    @y.setter
    def y(self, value):
        """ Sets y to value """
        self.integer_validate('y', value)
        self.__y = value

    def area(self):
        """" Returns rectangle area """
        return self.width * self.height

    def display(self):
        """
        Prints the rectangle
        print('\n'.join(['#' * self.width for rows in range(self.height)]))
        """
        if self.width == 0 or self.height == 0:
            print('')
            return
        [print("") for i in range(self.y)]
        for i in range(self.height):
            [print(' ', end='') for j in range(self.x)]
            [print('#', end='') for k in range(self.width)]
            print('')

    def __str__(self):
        """ returs string rep of the rectangle """
        return ("[Rectangle] " + '(' + str(self.id) + ')' + ' ' +
                str(self.x) + '/' + str(self.y) + ' - ' + str(self.width)
                + '/' + str(self.height))

    def set(self, id=None, width=None, height=None, x=None, y=None):
        """ Sets an argument to each attribute """
        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """ Assigns an argument to each attribute """
        if args:
            self.set(*args)
        elif kwargs:
            self.set(**kwargs)

    def to_dictionary(self):
        """ Returns the dictionary representation of a Rectangle """
        return {'x': self.x, 'y': self.y, 'id': self.id,
                'height': self.height, 'width': self.width}
