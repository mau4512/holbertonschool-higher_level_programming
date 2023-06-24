#!/usr/bin/python3
"""Defines a function that creates an Object from a JSON file"""
import json


def load_from_json_file(filename):
    """Create a Python object from a JSON file
    Args:
        filename: file from we created an object
    """
    with open(filename) as f:
        return json.load(f)
