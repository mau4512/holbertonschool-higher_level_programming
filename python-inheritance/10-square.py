#!/usr/nom/python3
"""Defines a Square class that is a subclass of Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represnet a square"""

    def __init__(self, size):
        """Initialize a new square
        Args:
            size: The size of the new square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
