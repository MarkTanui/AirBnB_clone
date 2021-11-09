#!/usr/bin/python3
""" 0x00. AirBnB clone - The console """
import json
from os import path


class FileStorage():
    """Class meant to manage JSON file storage for `BaseModel` and its child
    classes.
    Attributes:
        __file_path (str): default path to save JSON serializations to file
        __objects (dict): dict of items with `BaseModel` and its child classes
            as values, and '<object class name>.<object.id>' as keys
    Project tasks:
        5. Store first object
    """

    __file_path = "object_contents.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        new_objects = {}
        for key in self.__objects:
            new_objects[key] = self.__objects[key].to_dict()
        with open(self.__file_path, "w") as file:
            file.write(json.dumps(new_objects))

    def reload(self):
        """deserializes the JSON file to __objects, only if the JSON file"""
        """__file_path exists ; otherwise, do nothing. If the file doesnt"""
        """exist, no exception should be raised"""

        from ..base_model import BaseModel
        from ..user import User
        from ..state import State
        from ..city import City
        from ..amenity import Amenity
        from ..place import Place
        from ..review import Review

        classes = [BaseModel, User, State, City, Amenity, Place, Review]
        class_dict = dict()
        for c in classes:
            class_dict[c.__name__] = c

        if path.exists(self.__file_path):
            try:
                with open(self.__file_path, "r") as file:
                    new_objects = json.load(file)
                for key, value in new_objects.items():
                    self.__objects[key] = eval(value['__class__'])(**value)
            except:
                pass
