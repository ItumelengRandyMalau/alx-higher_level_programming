#!/usr/bin/python3
"""Defines a function that checks if a class is an instance
    of a given class."""


def is_same_class(obj, a_class):
    """Returns True if the object is exactly an
    instance of the specified class, otherwise False.
    
    Args:
        obj: The abject to check.
        a_class: The class type to match obj  type with.
        Returns:
            True is obj is an exact instance of a class, else false.
    """
    return type(obj) is a_class
