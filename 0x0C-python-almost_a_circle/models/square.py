#!/usr/bin/python3
"""Defines a square class(child class)."""
from rectangle import Rectangle


class Square(Rectangle):
    """Represents the Square class."""
    def __init__(self, size, x=0, y=0, id=None):
        """The Square constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Represents the  new str method for the child"""
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)
