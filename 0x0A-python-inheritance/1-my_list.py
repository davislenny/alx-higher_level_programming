#!/usr/bin/python3
"""
The '1-my_list' module
Defines the 'Mylist' class
"""


class MyList(list):
    """Define Mylist functons"""
    def print_sorted(self):
        """prints a sorted list"""
        print(sorted(self))
