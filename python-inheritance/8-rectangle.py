#!/usr/bin/python3
"""Defines a cllas Rectangle that is gonna inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """represent a rectangle using BaseGeomtry"""

    def __init__(self, width, height):
        """Initialize rectangle
        Args:
            width: The witdh of the Rectangle
            Height: The height of the rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
