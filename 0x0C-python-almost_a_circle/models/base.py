#!/usr/bin/python3
""" Defines a class named Base"""


class Base:
    """ Represents the Base model class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """ Contstructor to initialize class attributes"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
