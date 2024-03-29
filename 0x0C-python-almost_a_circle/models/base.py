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

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs
        to a file
        Args:
            list_objs(lis): list of instances who inherits of
            Base - example: list of Rectangle or list of
            Square instances.
        """
        f_name = "{}.json".format(cls.__name__)
        with open(f_name, "w") as json_file:
            if list_objs is None:
                json_file.write("[]")
            else:
                list_dic = []
                for obj in list_objs:
                    list_dic.append(obj.to_dictionary())
                json_file.write(Base.to_json_string(list_dic))

    def from_json_string(json_string):
        """
        Converts a json string to python list
        Args:
            json_string(str).
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Represents a class method that returns an instance with all
        attributes already set.
        Args:
            **dictionary(dict): can be thought of as a double
            pointer to a dictionary.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                dummy = cls(1, 1)
            else:
                dummy = cls(1)
            dummy.update(**dictionary)
            return dummy
    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances."""
        fileName = "{}.json".format(cls.__name__)
        try:
            with open(fileName, "r")as jsonFile:
                list_dicts = Base.from_json_string(jsonFile.read())
                list_instances = []

                for dicts in list_dicts:
                    list_instances.append(cls.create(**dicts))
                return list_instances
        except FileNotFoundError:
            return []
