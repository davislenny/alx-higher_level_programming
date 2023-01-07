#!/usr/bin/python3
"""
Unittest for max_integer([...])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxinteger(unittest.TestCase):

    def test_values(self):
        """Test for when list has varying ints"""
        self.assertAlmostEqual(max_integer([3, 10, 7, 7]), 10)
        """Test for same ints in a list"""
        self.assertAlmostEqual(max_integer([9, 9, 9]), 9)
        """Test for one element"""
        self.assertAlmostEqual(max_integer([11]), 11)
        """Test for when list has negative ints"""
        self.assertAlmostEqual(max_integer([-2, -4, -6, -9]), -2)
        """Test for same negative ints"""
        self.assertAlmostEqual(max_integer([-5, -5, -5]), -5)

        """Test for all float"""
        self.assertAlmostEqual(max_integer([0.225, 0.985, 0.333, 0.789]), 0.985)

        """Test alphabets and strings"""
        self.assertAlmostEqual(max_integer(['a', 'c', 'e', 'g']), 'g')
        self.assertAlmostEqual(max_integer([["aaa"], ["ccc"], ["eee"], ["ggg"]]), ["ggg"])
        self.assertAlmostEqual(max_integer("string"), "t")

    def test_None(self):
        """Test for an empty list"""
        self.assertAlmostEqual(max_integer([]), None)

    def test_types(self):
        """Raises type error if not list or if list elements cannot be compared"""
        with self.assertRaises(TypeError):
            max_integer([2, 5, "string"])
        """An int"""
        with self.assertRaises(TypeError):
            max_integer(104)
        """A float"""
        with self.assertRaises(TypeError):
            max_integer(108.232)       
