#!/usr/bin/python3
"""
The '100-my_int' module
"""


class MyInt(int):
    """MyInt has == and != operators inverted"""
    def __init__(self, num):
        """Initiate num"""
        self.num = num

    def __eq__(self, other):
        """Inverts '==' to '!='"""
        return self.num != other

    def __ne__(self, other):
        """Inverts '!=' to '=='"""
        return self.num == other
