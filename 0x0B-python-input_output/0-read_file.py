#!/usr/bin/python3
"""Defines a function that reads & prints a text file to STDOUT."""


def read_file(filename=""):
    """Reads and prints the contents of a UTF8 text file to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
