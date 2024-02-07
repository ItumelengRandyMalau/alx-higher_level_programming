#!/usr/bin/python3
# 6-from_json_string.py
"""Defines a JSON-to-object function."""
import json


def from_json_string(my_str):
    """Defines the Python object representation of a JSON string.
    Args:
        my_str(str): json represantation to convert to str.
    Returns:
        The Python object representation of a JSON string.
    """
    return json.loads(my_str)
