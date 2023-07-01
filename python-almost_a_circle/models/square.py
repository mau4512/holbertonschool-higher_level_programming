#!/usr/bin/python3
"""Defines a Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square
        Args:
            size: the size of the new square
            x: The coordinate x of the new square
            y: The coordinate y of the new square
            id: the identity of the new square
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return the print() and str() representation of a Square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
