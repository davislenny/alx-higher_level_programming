#!/usr/bin/python3
"""
The 'base' module
Defines the class 'base'
"""
import json


class Base:
    """class definition"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor"""
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns the JSON string representation of list_dictionaries """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes the JSON string representation of list_objs to a file """
        if list_objs is not None:
            list_objs = [obj.to_dictionary() for obj in list_objs]
        with open("{}.json".format(cls.__name__), mode='w', encoding='utf-8') as fd:
           fd.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """ Returns the list of the JSON string representation json_string """
        if json_string is None or json_string == []:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Returns an instance with all attributes already set """
        if cls.__name__ == 'Rectangle':
            size = cls(2, 3)
        if cls.__name__ == 'Square':
            size = cls(4)
        size.update(**dictionary)
        return size

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances """
        file_name = cls.__name__ + '.json'
        List = []
        try:
            with open(file_name, 'r') as fd:
                dictionary = cls.from_json_string(fd.read())
            for i, line in enumerate(dictionary):
                List.append(cls.create(**dictionary[i]))
        except:
            pass
        return List
