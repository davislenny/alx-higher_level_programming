#!/usr/bin/python3
"""
Base module
# run with python3 -m unittest tests/test_models/test_base.py
or python3 -m unittest discover tests
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle

# Rectangle = __import__('rectangle').Rectangle
import json
# Square = __import('square').Square


class TestBase(unittest.TestCase):
    """ Test Base class """

    def setUp(self):
        Base._Base__nb_objects = 0
        pass

    def tearDown(self):
        try:
            os.remove("Rectangle.json")
        except:
            pass

    def test_class_type(self):
        """ Test class instance """
        self.assertTrue(Base(9), self.__class__ == Base)

    def test_with_id(self):
        """ if id is not None """
        self.assertTrue(Base(10), self.id == 10)
        self.assertTrue(Base(0), self.id == 0)
        self.assertTrue(Base(1), self.id == 1)
        self.assertTrue(Base(-10), self.id == -10)

    def test_without_id(self):
        """ if id is None """
        self.assertTrue(Base(), self.id == 1)
        self.assertTrue(Base(), self.id == 2)

    def test_positional_args(self):
        """ Test for additional args """
        with self.assertRaises(TypeError):
            Base(9, 10)

    def test_private_attr(self):
        """ test __nb_objects access """
        with self.assertRaises(AttributeError):
            print(Base.__nb_objects)

    def test_to_json_string(self):
        """ with a dictionary """
        L1 = {'id': 89, 'width': 10, 'height': 4}
        str1 = Base.to_json_string([L1])
        self.assertTrue(type(L1) == dict)
        self.assertTrue(type(str1) == str)

        """ With a None """
        L2 = None
        str2 = Base.to_json_string([L2])
        self.assertTrue(type(str2) == str)
        self.assertTrue(str2, "[]")

        """ With empty dict """
        L3 = dict()
        str3 = Base.to_json_string([L3])
        self.assertTrue(len(L3) == 0)
        self.assertTrue(type(str3) == str)
        self.assertTrue(str3, "[]")

    def test_save_to_file(self):
        """ With a list instance """
        r1 = Rectangle(10, 7, 2, 8)
        Rectangle.save_to_file([r1])
        with open("Rectangle.json", "r") as file:
             self.assertEqual(json.dumps([r1.to_dictionary()]), file.read())

        """ When list is None """
        r2 = None
        Rectangle.save_to_file(r2)
        with open("Rectangle.json", "r") as file:
            self.assertEqual('[]', file.read())

    def test_from_json_string(self):
        """ string to dict """
        L0 = '[{"height": 4, "width": 10, "id": 89}]'
        str0 = Base.from_json_string(L0)
        self.assertTrue(type(L0) == str)
        self.assertTrue(type(str0) == list)
        self.assertTrue(type(str0[0]) == dict)

        """ When json_string is None """
        L1 = None
        str1 = Base.from_json_string(L1)
        self.assertTrue(type(str1) == list)
        self.assertTrue(str1 == [])

        """ When json_string is empty """
        L2 = "" 
        str2 = Base.from_json_string(L2)
        self.assertTrue(type(str2) == list)
        self.assertTrue(str2 == [])

    def test_create(self):
        """ Create attributes """
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r1), '[Rectangle] (1) 1/0 - 3/5')
        self.assertEqual(str(r2), '[Rectangle] (1) 1/0 - 3/5')
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)

    def test_load_from_file(self):
        """ With a file present and has json string """
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        rect = Rectangle.load_from_file()
        self.assertEqual(len(rect), 2)
        for i, line in enumerate(rect):
            if i == 0:
                self.assertEqual(str(line), '[Rectangle] (1) 2/8 - 10/7')
            if i == 1:
                self.assertEqual(str(line), '[Rectangle] (2) 0/0 - 2/4')

        """ File present but empty """
        Rectangle.save_to_file([])
        rect = Rectangle.load_from_file()
        self.assertEqual(type(rect), list)
        self.assertEqual(len(rect), 0)
