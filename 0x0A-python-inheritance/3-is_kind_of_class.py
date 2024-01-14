#!/usr/bin/python3
"""Defines a class and inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """Checks if an object is an instance of or inherited instance of a class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj against.
    Returns:
        True if obj is an instance of or inherited instance of a_class.
        Otherwise - False.
    """
    if isinstance(obj, a_class):
        return True
    return False
