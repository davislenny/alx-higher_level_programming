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

    @property
    def to_json(self):
        """returns/retrieves a dictionary represenation of
        class student
        """
        return student.__dict__
