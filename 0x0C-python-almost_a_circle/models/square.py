#!/usr/bin/python3
""" square """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ classs definition """
    def __init__(self, size, x=0, y=0, id=None):
        """ Constructor """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Returns string rep of the square """
        return '[{}] ({}) {}/{} - {}'.format(
                type(self).__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """ returns the size of the square """
        return self.height

    @size.setter
    def size(self, value):
        """ sets size(width and height) to value """
        self.width = value
        self.height = value

    def set(self, id=None, size=None, x=None, y=None):
        """ sets args and kwargs """
        if id is not None:
            self.id = id
        if size is not None:
            self.height = size
            self.width = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """ sets attributes to args or kwargs """
        if args:
            self.set(*args)
        elif kwargs:
            self.set(**kwargs)

    def to_dictionary(self):
        """ Returns a dict of Square """
        return {'id': self.id, 'x': self.x, 'size': self.width, 'y': self.y}
