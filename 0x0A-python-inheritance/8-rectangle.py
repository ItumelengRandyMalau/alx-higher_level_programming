#!/usr/bin/python3
"""
   Rectangle that inherits from BaseGeometry (7-base_geometry.py).
   Args: width and height.
   These parameters are validated by "interger_validator.
   """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height
