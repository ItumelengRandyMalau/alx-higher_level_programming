#!/usr/bin/python3
"""Defines a square class(child class)."""
from rectangle import Rectangle


class Square(Rectangle):
    """Represents the Square class."""
    def __init__(self, size, x=0, y=0, id=None):
        """The Square constructor"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """Represents the  new str method for the child"""
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)
