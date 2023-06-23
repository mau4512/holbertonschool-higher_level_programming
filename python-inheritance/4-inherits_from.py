#!/usr/bin/python3
"""Defines an inherited class-checking function"""


def inherits_from(obj, a_class):
    """Checks if an object is an inherited instance of a class
    Args:
        obj: The object to check
        a_class: The class to match the typt of obj to
    Returns
        True - if the object is an inherited of a class
        False - Otherwise
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return (True)
    return(False)
