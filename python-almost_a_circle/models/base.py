#!/usr/bin/python3
"""Defines a base class"""
import json
import csv


class Base:
    """Represnet the base model
    Represents de "base" for all other classes in project
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base
        Args:
            id(int): The identity of the new Base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON serialization of a list of dicts
        Args:
            list_dictionaries: A list of dictionaries
        """
        if list_dictionaries in None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def created(cls, **dictionary):
        """Returns a class instatied from a dictionary of attributes
        Args:
            **dictionary: hey/value pair of attributes to initialize
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new
