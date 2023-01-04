#!/usr/bin/python3
"""
The 'lockedclass' module
"""


class LockedClass:
    """
    prevents the user from dynamically creating a
    new instance attributes except if the
    new instance attribute is called first_name
    """
    __slots__ = 'first_name',
