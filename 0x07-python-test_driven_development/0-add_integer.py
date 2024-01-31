#!/usr/bin/python3
""" This module contains the add function,
it adds two integers and returns their sum
"""


def add_integer(a, b=98):
    """
    This function adds integer a, and b.
    Args:
        a(integer): First number.
        b(integer): Second number.
    Returns:
        The sum of a and b(integer).
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    # Convering a and b to intgers
    a = int(a)
    b = int(b)
    return a + b
