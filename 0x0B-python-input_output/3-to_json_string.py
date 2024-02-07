#!/usr/bin/python3
""" Defines a function that returns the JSON
    representation of an object (string):"""
import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object.
    Args:
        my_obj(str): Data to convert to JSON.
        Returns: JSON represantation of "my_obj"
    """
    return json.dumps(my_obj)
