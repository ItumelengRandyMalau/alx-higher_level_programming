#!/usr/bin/python3
""" This module includes a function that returns
    a list of available attributes and methods of an object"""


def lookup(obj):
    """Returns a list of available attributes and
    methods of an object."""
    return (dir(obj))
