#!/usr/bin/python3
"""
The square module
# run the test with python3 -m unittest tests/test_models/test_square.py
or with python3 -m unittest discover tests
"""
import unittest
from models.square import Square
from io import StringIO
from contextlib import redirect_stdout


class TestSquare(unittest.TestCase):
    """ Test class Square """

    def test_class(self):
        """ test square class instance """
        s1 = Square(4)
        self.assertEqual(type(s1), Square)

    def test_attributes(self):
        """ All attr present """
        s2 = Square(6, 3, 4, 11)
        self.assertTrue(s2.size == 6)
        self.assertTrue(s2.width == 6)
        self.assertTrue(s2.height == 6)
        self.assertTrue(s2.x == 3)
        self.assertTrue(s2.y == 4)
        self.assertTrue(s2.id == 11)

        """ Test size arg """
        s3 = Square(10)
        self.assertTrue(s3.size == 10)
        self.assertTrue(s3.width == 10)
        self.assertTrue(s3.height == 10)
        self.assertTrue(s3.x == 0)
        self.assertTrue(s3.y == 0)
        self.assertTrue(s3.id is not None)

    def test_types(self):
        """ Non-integer attr """
        with self.assertRaises(TypeError):
            Square()
            Square(None)
            Square(12, 1, 3, 11, 5)
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            Square([2])
            Square('5')
            Square({'a': 12})
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            Square(4, '2', 3)
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            Square(5, 3, [2])

    def tests_values(self):
        """ Tests ValueErrors """
        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            Square(-4)
            Square(0)
        with self.assertRaisesRegex(ValueError, 'x must be >= 0'):
            Square(5, -1, 3)
        with self.assertRaisesRegex(ValueError, 'y must be >= 0'):
            Square(9, 2, -3)

    def test_str(self):
        """ Test string rep fof the square """
        s3 = Square(3, 1, 3, 10)
        self.assertEqual(str(s3), '[Square] (10) 1/3 - 3')
        s3.size = 6
        self.assertEqual(str(s3), '[Square] (10) 1/3 - 6')

    def test_display(self):
        """print square"""
        with StringIO() as Sq, redirect_stdout(Sq):
            s4 = Square(3)
            s4.display()
            s = Sq.getvalue()
        self.assertEqual(s, '###\n###\n###\n')
        with StringIO() as Sq, redirect_stdout(Sq):
            s4 = Square(4, 2, 2)
            s4.display()
            s = Sq.getvalue()
        self.assertEqual(s, '\n\n  ####\n  ####\n  ####\n  ####\n')

    def test_update(self):
        """ test update method """
        s1 = Square(5, 0, 0, 1)
        self.assertEqual(str(s1), '[Square] (1) 0/0 - 5')
        s1.update(10)
        self.assertEqual(str(s1), '[Square] (10) 0/0 - 5')
        s1.update(1, 2)
        self.assertEqual(str(s1), '[Square] (1) 0/0 - 2')
        s1.update(1, 2, 3, 4)
        self.assertEqual(str(s1), '[Square] (1) 3/4 - 2')
        """ using **kwargs """
        s1.update(x=12)
        self.assertEqual(str(s1), '[Square] (1) 12/4 - 2')
        s1.update(size=7, y=1)
        self.assertEqual(str(s1), '[Square] (1) 12/1 - 7')
        s1.update(size=7, id=89, y=1)
        self.assertEqual(str(s1), '[Square] (89) 12/1 - 7')

    def test_to_dictionary(self):
        """ test return square dict """
        s1 = Square(10, 2, 1, 1)
        s1_dict = s1.to_dictionary()
        self.assertEqual(type(s1_dict), dict)
        self.assertEqual(str(s1_dict), "{'id': 1, 'x': 2, 'size': 10, 'y': 1}")
        s2 = Square(1, 1)
        s2.update(**s1_dict)
        self.assertEqual(str(s2), str(s1))
