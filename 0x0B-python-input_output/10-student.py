#!/usr/bin/python3
"""
The '8-students' module
Defines the class 'Student'
"""


class Student:
    """Initiate attributes"""
    def __init__(self, first_name, last_name, age):
        """Constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns/retrieves a dictionary represenation of
        class student
        """
        if attrs is None:
            return self.__dict__.copy()
        else:
            j_dict = {}
            for key in attrs:
                if key in self.__dict__.keys():
                    j_dict[key] = self.__dict__[key]
            return j_dict
