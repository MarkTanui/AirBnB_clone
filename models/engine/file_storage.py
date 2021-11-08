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

