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