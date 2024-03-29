#!/usr/bin/python3
"""
 This module contains a function that prints: my name is
 <first_name> <last_name>.
 """


def say_my_name(first_name, last_name=""):
    """
    prints the string "My name is <first_name> <last_name>".
    Args:
        first_name: First argument.
        last_name: Second argument.
        Return:
        str: My name is <first_name> <last_name>.
        """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
