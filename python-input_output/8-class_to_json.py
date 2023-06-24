#1/usr/bin/python3
"""Defines a Python class to JSON function"""


def class_to_json(obj):
    """Return the dictionary representation of a simple data structrure
    Args:
        obj: is a instance of a Class
    """
    return obj.__dict__
