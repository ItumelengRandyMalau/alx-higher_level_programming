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
        """Gets the size of the Squeare"""
        return self.width

    @size.setter
    def size(self, value):
        """sets the size of the Square"""
        self.width = value
        self.height = value

    def __str__(self):
        """Represents the  new str method for the child"""
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """Assigns arguments to attributes based on their order"""
        if args:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.size = arg
                if i == 2:
                    self.x = arg
                if 1 == 3:
                    self.y = arg
                else:
                    break
        elif len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.width = value
                    self.height = vale
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value
                else:
                    break

    def to_dictionary(self):
        """A dictionary representation of a square """
        square_dic = {
                "id": self.id,
                "size": self.width,
                "x": self.x,
                "y": self.y
            }
        return square_dic
