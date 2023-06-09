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
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """write the JSON serialization of a list of obbjetcs to a file
        Args:
            list_objs: a list of inherited Base instances
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return the deserialization of a JSON string
        Args:
            json_string: a JSON str representation of a list of dicts.
        returns:
            if json_string is None or empty - an empty list
            otherwise - the python list represented by json_string
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns a class instatied from a dictionary of attributes
        Args:
            **dictionary: key/value pair of attributes to initialize
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """Return a list of classes instatiated from a CSV file
        reads from <cls.__name__>.csv
        Returns:
         if the file does not exist - an empty list
         otherwise - a list of instatiated classes
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
