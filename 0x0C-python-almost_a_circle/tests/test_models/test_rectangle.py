#!/usr/bin/python3
"""
The rectangle module
# Run test with python3 -m unittest tests/test_models/test_rectangle.py
or with python3 -m unittest discover tests
"""
import unittest
from models.rectangle import Rectangle
from contextlib import redirect_stdout
from io import StringIO


class TestRectangle(unittest.TestCase):
    """ Test class Rectangle """

    def test_class(self):
        """ tests class instance """
        self.assertEqual(type(Rectangle(3, 4)), Rectangle)

    def test_attributes(self):
        """ All attributes present """
        r1 = Rectangle(10, 2, 0, 0, 12)
        self.assertTrue(r1.width == 10)
        self.assertTrue(r1.height == 2)
        self.assertTrue(r1.x == 0)
        self.assertTrue(r1.y == 0)
        self.assertTrue(r1.id == 12)

        """ Test id not parsed"""
        r2 = Rectangle(10, 2)
        self.assertTrue(r2.id is not None)
        r3 = Rectangle(2, 10)
        self.assertTrue(r3.id is not None)

    def test_types(self):
        """ Non-integer attributes """
        with self.assertRaises(TypeError):
            Rectangle()
            Rectangle(None)
            Rectangle(5)
            Rectangel(1, 2, 3, 4, 5, 6)
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            Rectangle([2], 5)
            Rectangle('5', 3)
            Rectangle(None, 4)
        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            Rectangle(2, [5])
            Rectangle(5, '3')
            Rectangle(4, None)
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            Rectangle(2, 4, '5', 0)
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            Rectangle(3, 6, 7, None)

    def test_values(self):
        """ width and height """
        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            Rectangle(0, 9)
            Rectangle(-9, 5)
        with self.assertRaisesRegex(ValueError, 'height must be > 0'):
            Rectangle(8, 0)
            Rectangle(6, -3)

        """ x and y """
        with self.assertRaisesRegex(ValueError, 'x must be >= 0'):
            Rectangle(3, 5, -1, 0)
        with self.assertRaisesRegex(ValueError, 'y must be >= 0'):
            Rectangle(5, 3, 8, -4)

    def test_private_attr(self):
        """ try accessing all attributes """
        with self.assertRaises(AttributeError):
            print(Rectangle.__width)
            print(Rectangle.__height)
            print(Rectangle.__x)
            print(Rectangle.__y)

    def test_area(self):
        """ test public method area() """
        r1 = Rectangle(3, 2)
        r2 = Rectangle(2, 10, 1, 1)
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r1.area(), 6)
        self.assertEqual(r2.area(), 20)
        self.assertEqual(r3.area(), 56)

    def test_display(self):
        """ test public method display() """
        r1 = Rectangle(4, 3)
        r2 = Rectangle(4, 3, 1, 2)
        with StringIO() as rec, redirect_stdout(rec):
            r1.display()
            rect = rec.getvalue()
        self.assertEqual(rect, '####\n####\n####\n')
        with StringIO() as rec, redirect_stdout(rec):
            r2.display()
            rect = rec.getvalue()
        self.assertEqual(rect, '\n\n ####\n ####\n ####\n')

    def test__str(self):
        """ test print rectangle in __str__ format """
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertTrue(str(r1) == '[Rectangle] (12) 2/1 - 4/6')

    def test_update(self):
        """ test the update method """
        r1 = Rectangle(10, 10, 10, 10)
        """ test args with atrr order """
        r1.update(89)
        self.assertEqual(str(r1), '[Rectangle] (89) 10/10 - 10/10')
        r1.update(89, 2)
        self.assertEqual(str(r1), '[Rectangle] (89) 10/10 - 2/10')
        r1.update(89, 2, 3)
        self.assertEqual(str(r1), '[Rectangle] (89) 10/10 - 2/3')
        r1.update(89, 2, 3, 4)
        self.assertEqual(str(r1), '[Rectangle] (89) 4/10 - 2/3')
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r1), '[Rectangle] (89) 4/5 - 2/3')

        """ test with **kwargs """
        r1.update(height=1)
        self.assertEqual(str(r1), '[Rectangle] (89) 4/5 - 2/1')
        r1.update(width=1, x=2)
        self.assertEqual(str(r1), '[Rectangle] (89) 2/5 - 1/1')
        r1.update(y=1, width=2, x=3, id=7)
        self.assertEqual(str(r1), '[Rectangle] (7) 3/1 - 2/1')
        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(r1), '[Rectangle] (7) 1/3 - 4/2')

    def test_to_dictionary(self):
        """ returs a dict rep of the rectangle """
        r1 = Rectangle(10, 2, 1, 9, 90)
        r1_dictionary = r1.to_dictionary()
        self.assertEqual(type(r1_dictionary), dict)
        r2 = Rectangle(1, 1)
        r2.update(**r1_dictionary)
        self.assertEqual(str(r2), '[Rectangle] (90) 1/9 - 10/2')
