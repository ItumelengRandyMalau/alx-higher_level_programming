#!/usr/bin/pyithon3
"""
   Rectangle that inherits from BaseGeometry (7-base_geometry.py).
   Args:
        width(int): width of a new rectangle
        height(int): height of a new rectangle.
   These parameters are validated by "interger_validator.
   """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle using BaseGeometry."""
    def __init__(self, width, height):
        """ Initializes a new Rectangle."""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
