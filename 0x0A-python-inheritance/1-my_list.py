#!/usr/bin/python3
"""Defines an class:MyList, which inherits from list."""


class MyList(list):
    """Implements "MyList" class."""

    def print_sorted(self):
        """Prints a list sorted in ascending order."""
        print(sorted(self))
