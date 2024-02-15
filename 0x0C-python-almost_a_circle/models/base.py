#!/usr/bin/python3
""" Defines a class named Base"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """"
        Returns the represantation of a JSON-string
        derived from "list_dictionaries"
        Args:
            list_dictionaries(dictionary): data to convert to
            JSON string
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        str_json = json.dumps(list_dictionaries)
        return str_json
